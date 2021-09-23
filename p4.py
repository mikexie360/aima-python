#Mike Xie
# this program tests the heuristic of the flight distance and road map
from numpy import array
from utils import *
from search import *

#flight path to dallas
"""
Austin          182
Charlotte       929
San Francisco   1230
Los Angeles     1100
New York        1368
Chicago         800
Seattle         1670
Santa Fe        560
Bakersville     1282
Boston          1551
"""
#flight path to dallas in order of distance
"""
"""
flightPath=[
        ["Dallas", 0],
        ["Austin",182],
        ["Charlotte",929],
        ["San Francisco", 1230],
        ["Los Angeles", 1100],
        ["New York",1368],
        ["Chicago", 800],
        ["Seattle",1670],
        ["Santa Fe",560],
        ["Bakersville",1282],
        ["Boston", 1551]]

def bubbleSort(flight):
    length = len(flight)

    for i in range(length -1):
        for j in range(0, length - i -1):
            if flight[j][1] > flight[(j+1)][1]:
                flight[j], flight[(j+1)] = flight[(j+1)], flight[j]

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
    def printSolution(self, dist):
        print("Dallas to other cities through road")
        for node in range(self.V):
            print("Dallas to",flightPath[node][0],"road distance",flightPath[node][1], "flight distance", dist[node])
    def minDistance(self, dist, sptSet):
 
        # Initialize minimum distance for next node
        min = sys.maxsize
 
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index

    def dijkstra(self, src):
 
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
 
        self.printSolution(dist)

def main():
    

    # now sort it to get in order
    bubbleSort(flightPath)
    # sorted flight path looks like this
    """
    [['Dallas', 0],
    ['Austin', 182], 
    ['Santa Fe', 560], 
    ['Chicago', 800], 
    ['Charlotte', 929], 
    ['Los Angeles', 1100], 
    ['San Francisco', 1230], 
    ['Bakersville', 1282], 
    ['New York', 1368], 
    ['Boston', 1551], 
    ['Seattle', 1670]]
    """
    # now flight path is in order
    
    roadPath=[
        # Dallas, Austin, Santa Fe, Chicago, Charlotte, Los Angeles, San Francisco, Bakersville, New York, Boston, Seattle
        [0,         195,    640,    0,          0,      0,              0,              0,          1548,   0,       0], # Dallas
        [195,       0,       0,      0,         1200,   1377,           0,          0,              0,      1963,   0], # Austin
        [640,       0,       0,      1272,      0,      0,              0,              864,          0,         0,   1463], # Santa Fe
        [0,         0,      1272,          0,      0,      0,              0,              0,        0,       983,   2064], # Chicago
        [0,         1200,      0,          0,      0,          0,          0,              0,         634,        0,       0,], # Charlotte
        [0,         1377,          0,       0,        0,       0,          383,          153,          0,          0,      0], # Los Angeles
        [0,         0,          0,      0,          0,      383,          0,              283,          0,      3095,      807], # San Francisco
        [0,         0,          864,      0,          0,       153,             283,       0,          0,       0,         0],  # Bakersville
        [1548,         0,          0,          0,     634,         0,          0,              0,       0,      225,      0], # New York
        [0,         1963,       0,       983,      0,      0,          3095,              0,        225,    0,           0], # Boston
        [0,         0,          1463,      2064,      0,          0,          807,          0,              0,         0,       0]  # Seattle
    ]
    r = Graph(11)
    r.graph = roadPath

    r.dijkstra(0)   # all path costs to dallas

    print("""
    The heuristic is inconsistent.
    You can see that although Charlotte has higher hueristic/flight distance than Chicago, 
    Charlotte's road path to dallas is actually shorter than Chicago's road path to dallas.
    Making the heuristic inconsistent
    """)
main()