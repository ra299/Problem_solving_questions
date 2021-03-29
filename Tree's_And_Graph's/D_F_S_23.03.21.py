from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, v, u):
        self.graph[v].append(u)

    def dfsN(self,v, visited):
        visited.add(v)
        print(v, end = " ")
        for i in self.graph[v]:
            if i not in visited:
                self.dfsN(i, visited)

    def dfs(self, v):
        visited = set()

        self.dfsN(v, visited)

if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    
    print("Following is DFS from (starting from vertex 2)")
    g.dfs(2)
 
