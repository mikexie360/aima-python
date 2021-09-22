# Mike Xie

# Searching for road trips in the USA

## You contemplate to search for a trip back to dallas from seattle, having access to a road map, which should be implemented as a graph

## find the solution and return a simulation of the RBFS strategy by generating
## automatically the following five values
# f limit
# best
# alternative
# current-city
# next-city
# for each node visited

# find the same solution manually for each node visited for each of the five values

from utils import *
from search import *
from collections import deque

import math
def recursive_best_first_search(problem, h=None):
	"""[Figure 3.26]"""
	h = memoize(h or problem.h, 'h')

	def RBFS(problem, node, flimit):
		if problem.goal_test(node.state):
			return node, 0  # (The second value is immaterial)
		successors = node.expand(problem)
		if len(successors) == 0:
			return None, np.inf
		for s in successors:
			s.f = max(s.path_cost + h(s), node.f)
		while True:
			# Order by lowest f value
			successors.sort(key=lambda x: x.f)
			best = successors[0]
			if best.f > flimit:
				return None, best.f
			if len(successors) > 1:
				alternative = successors[1].f
			else:
				alternative = np.inf
			print("\n")
			print("f limit = ", flimit)
			print("best ", best.f)
			print("alternative", alternative)
			print("current", node.state)
			print("next city", best.state)
			print("\n")
			result, best.f = RBFS(problem, best, min(flimit, alternative))
			if result is not None:
				return result, best.f

	node = Node(problem.initial)
	node.f = h(node)
	result, bestf = RBFS(problem, node, np.inf)
	return result
def astar_search(problem, h=None, display=False):
    """A* search is best-first graph search with f(n) = g(n)+h(n).
    You need to specify the h function when you call astar_search, or
    else in your Problem subclass."""
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, lambda n: n.path_cost + h(n), display)

def best_first_graph_search(problem, f, display=False):
	f = memoize(f, 'f')
	node = Node(problem.initial)
	frontier = PriorityQueue('min', f)
	frontier.append(node)
	explored = set()
	while frontier:
		node = frontier.pop()
		if problem.goal_test(node.state):
			if display:
				print(len(explored), "paths have been expanded and", len(frontier), "paths remain in the frontier")
			return node
		explored.add(node.state)
		for child in node.expand(problem):
			if child.state not in explored and child not in frontier:
				frontier.append(child)
			elif child in frontier:
				if f(child) < frontier[child]:
					del frontier[child]
					frontier.append(child)
		print("[Current node:",node,"; Evaluation function=",node.f,";\nExplored Cities=",explored,";Frontier:",frontier,";")
	return None

# problems will be solved with various search algorithms
road_map = UndirectedGraph(dict(
	LosAngeles=dict(SanFrancisco=383, Austin=1377, Bakersville=153),
	SanFrancisco=dict(Bakersville=283, Seattle=807),
	Seattle=dict(SantaFe=1463, Chicago=2064),
	Bakersville=dict(SantaFe=864),
	Austin=dict(Dallas=195, Charlotte=1200),
	SantaFe=dict(Dallas=640, Chicago=983),
	Boston=dict(Austin=1963, NewYork=225, Chicago=1272, SanFrancisco=3095),
	Dallas=dict(NewYork=1548),
	Charlotte=dict(NewYork=634)))

road_map.locations = dict(
	Dallas =(0,0), Austin=(182,0), Charlotte=(929,0), 
	SanFrancisco=(1230,0), LosAngeles=(1100,0),NewYork=(1368,0),
	Chicago=(800,0),Seattle=(1670,0),SantaFe=(560,0),
	Bakersville=(1282,0),Boston=(1551,0)
)

def main():
	# heuristic
	road_problem = GraphProblem('Seattle','Dallas', road_map)

	# RBFS
	print("RBFS")
	print("Solution")
	print(recursive_best_first_search(road_problem).solution())
	# A*
	print("\n\nAstar\n")
	print("List the contents of the frontier, explored list during search")
	print("\nSolution Path for Astar\n",astar_search(road_problem).solution())
main()
