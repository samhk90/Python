from collections import defaultdict
class bsf_graph:
    def __init__(self):
        self.graph=defaultdict(list)
        self.visited=[]

    def genrating_graph(self,edges):
        for i in edges:
            a, b = i[0], i[1]
            self.graph[a].append(b)
        print(self.graph)
    def bfs(self,s):
        queue=[]
        queue.append(s)
        self.visited.append(s)

        while queue:

            s = queue.pop(0)
            print(s, end=" ")
            for i in self.graph[s]:
                if i not in self.visited:
                    queue.append(i)
                    self.visited.append(s)


g=bsf_graph()
edges=[
    [0, 1], [2, 3],
    [0, 2], [3, 3],
    [1, 2], [2, 0]
]
g.genrating_graph(edges)
g.bfs(0)




