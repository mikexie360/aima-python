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



import math

# problems will be solved with various search algorithms
class Problem(object):
	def __init__(self, initial, goal=None):
		self.initial = initial
		self.goal = goal
	def actions(self, state):
		raise NotImplementedError
	def result(self, state, action):
		raise NotImplementedError
	# check if state is a goal
	def goal_test(self, state):
		if isinstance(self.goal, list):
			return is_in(state, self.goal)
		else:
			return state == self.goal
	#cost increase for every step in path
	def path_cost(self, c, state1, action, state2):
		return c + 1
	def value(self, state):
		raise NotImplementedError
class Node:
	def __init__(self, state, parent=None, action=None, path_cost=0):
		# Create a search tree node, made from parent from an action
		self.state = state
		self.parent = parent
		self.action = action
		self.path_cost = path_cost
		self.depth = 0
		if parent:
			self.depth = parent.depth + 1
	def __repr__(self):
		return "<Node {}>".format(self.state)
	def __lt__(self, node):
		return self.state < node.state
	def expand(self, problem):
		# list the nodes reachable in one step from this node
		return [self.child_node(problem, action)
			for action in problem.actions(self.state)]
	def child_node(self, problem, action):
		next_state = problem.result(self.state, action)
		next_node = Node(next_state, self, action, problem.path_cost(self.path_cost, self.state, action, next_state))
		return next_node
	def solution(self):
		# return the sequence of actions to go from the root to this node
		return [node.action for node in self.path()[1:]]
	def path(self):
		# the path of a node
		node, path_back = self, []
		while node:
			path_back.append(node)
			node = node.parent
		return list(reversed(path_back))
	def __eq__(self, other):
		return isinstance(other, Node) and self.state == other.state
	def __hash__(self):
		return hash(self.state)
class GraphProblem(Problem):
	def __init__(self, initial, goal, graph):
		Problem.__init__(self,initial, goal)
		self.graph = graph
	def actions(self, A):
		return list(self.graph.get(A).keys())
	def result(self, state, action):
		return action
	def path_cost(self, cost_so_far, A, action, B):
		return cost_so_far + (self.graph.get(A,B) or infinity)
	def find_min_edge(self):
		m = infinity
		for d in self.graph.graph_dict.values():
			local_min = min(d.values())
			m = min(m, local_min)
		return m
	def h(self, node):
		locs = getattr(self.graph, 'locations', None)
		if locs:
			if type(node) is str:
				return int(distance(locs[node], locs[self.goal]))
			return int(distance(locs[node.state], locs[self.goal]))
		else:
			return infinity

class Graph:
	def __init__(self, graph_dict=None, directed=True):
		self.graph_dict = graph_dict or {}
		self.directed = directed
		if not directed:
			self.make_undirected()
	def make_undirected(self):
		for a in list(self.graph_dict.keys()):
			for (b, dist) in self.graph_dict[a].items():
				self.connect1(b, a, dist)
	def connect(self, A, B, distance=1):
		self.connect(A, B, distance)
		if not self.directed:
			self.connect(B, A, distance)
	def connect1(self, A, B, distance):
		self.graph_dict.setdefault(A, {})[B] = distance
	def get(self, a, b=None):
		links = self.graph_dict.setdefaults(a, {})
		if b is None:
			return links
		else:
			return links.get(b)
	def nodes(self):
		s1 = set([k for k in self.graph_dict.keys()])
		s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
		nodes = s1.union(s2)
		return list(nodes)


def UndirectedGraph(graph_dict=None):
	return Graph(graph_dict=graph_dict, directed=False)

def recursive_best_first_search(problem, h=None):
	h = memoize(h or problem.h, 'h')

	def RBFS(problem, node, flimit):



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


def main():
	print("hi")
	road_problem = GraphProblem('Dallas','Seattle', road_map)
	print(nodes

main()
