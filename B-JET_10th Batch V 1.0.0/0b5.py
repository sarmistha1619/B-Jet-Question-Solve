from collections import defaultdict
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary
    def addEdge(self, v):
        self.graph.append([v])
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        else:
            parent[yroot] = xroot
            rank[xroot] += 1
    def KruskalMST(self):

        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph,key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:

            v, w = self.graph[i]
            i = i + 1

            y = self.find(parent, v)

        minimumCost = 0
        print("Edges in the constructed MST")
        for  v, weight in result:
            minimumCost += weight
            print("%d == %d" % ( v, weight))
        print("Minimum Spanning Tree", minimumCost)


# Driver code
g = Graph(4)

g.addEdge(0,1)
g.addEdge(1,1)
g.addEdge(2,3)
g.addEdge(3,3)
g.addEdge(4,6)
g.addEdge(5,4)
g.addEdge(6,5)
g.addEdge(7,6)
g.addEdge(8,2)
g.addEdge(9,4)
g.addEdge(10,2)
g.addEdge(11,7)
g.addEdge(12,2)

# Function call
g.KruskalMST()