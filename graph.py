#simple undricted graph using defaultdict
from collections import  defaultdict
def genrating_graph(edges):
    graph=defaultdict(list)
    for i in edges:
        a,b=i[0],i[1]
        graph[a].append(b)
        graph[b].append(a)
    return graph

edges=[
    ["A", "B"], ["A", "E"],
    ["A", "C"], ["B", "D"],
    ["B", "E"], ["C", "F"],
    ["C", "G"], ["D", "E"]
]
graph=genrating_graph(edges)
print(graph)
