import networkx as nx

f = open('input.txt')
lines = [x.strip() for x in f.readlines()]

DG = nx.DiGraph()

for line in lines:
    nodes = line.split(')')
    DG.add_weighted_edges_from([ (nodes[0], nodes[1],1)])

s = 0
for i in DG.nodes():
    if i == "COM":
        continue
    s += len(nx.shortest_path(DG,"COM",i)) -1

print(s)