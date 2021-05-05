from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_Edge(self,u,v):
        self.graph[u].append(v)

    def isReachable(self, s,d):
        visited = [False] * self.V
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:

            n = queue.pop(0)
            if n == d:
                return True

            for i in self.graph[n]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return False

if __name__ == "__main__":
    g = Graph(4)
    g.add_Edge(0, 1)
    g.add_Edge(0, 2)
    g.add_Edge(1, 2)
    g.add_Edge(2, 0)
    g.add_Edge(2, 3)
    g.add_Edge(3, 3)
    
    u =1; v = 3
    
    if g.isReachable(u, v):
        print("There is a path from %d to %d" % (u,v))
    else :
        print("There is no path from %d to %d" % (u,v))
    
    u = 3; v = 1
    if g.isReachable(u, v) :
        print("There is a path from %d to %d" % (u,v))
    else :
        print("There is no path from %d to %d" % (u,v))