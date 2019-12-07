import networkx as nx

f = open('input.txt')
lines = [x.strip() for x in f.readlines()]

G = nx.DiGraph()

for line in lines:
    nodes = line.split(')')
    G.add_edge(nodes[0], nodes[1])
    G.add_edge(nodes[1], nodes[0])


print(len(nx.shortest_path(G,"YOU", "SAN"))-3)