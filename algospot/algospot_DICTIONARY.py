### Python program to print topological sorting of a DAG
from collections import defaultdict
 
#Class to represent a graph
class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list) #dictionary containing adjacency List
        self.V = dict()
        self.Finished = dict()
        self.cycle = False
        for v in vertices:
            self.V[v] = False
            self.Finished[v] = False
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # A recursive function used by topologicalSort
    def topologicalSortUtil(self,v,stack): 
        # Mark the current node as visited.
        self.V[v] = True
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if not self.V[i]:
                self.topologicalSortUtil(i,stack)
            elif not self.Finished[i]:
                self.cycle = True
 
        # Push current vertex to stack which stores result
        self.Finished[v] = True
        stack.insert(0,v)
 
    # The function to do Topological Sort. It uses recursive 
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        stack =[]
 
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for k,v in self.V.items():
            if v != True:
                self.topologicalSortUtil(k,stack)
 
        # Print contents of the stack
        if not self.cycle:
            print(''.join(stack))
        else:
            print('INVALID HYPOTHESIS')
for i in range(int(input())):
    g = Graph(list('abcdefghijklmnopqrstuvwxyz'))
    words = []
    for j in range(int(input())):
        w = str(input())
        words.append(w)              
    for i, word in enumerate(words):
        if(i == (len(words)-1)):
            break
        l = min(len(words[i]), len(words[i+1]))
        for j in range(l):
            char1 = words[i][j]
            char2 = words[i+1][j]
            if(char1 != char2):
                g.addEdge(char1,char2)    
                break
    g.topologicalSort()