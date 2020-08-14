# Romel Pascua
# 017167304
# CECS 328 Final
# Dijkstra
from Node import *
from Dijkstra import *

# all nodes start with dst = infinity
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

# (node, weight)
a.adj = {(b, 15), (c, 2), (d, 3)}
b.adj = {(a, 15), (c, 8), (e, 2), (f, 1)}
c.adj = {(a, 2), (b, 8), (f, 7), (g, 5)}
d.adj = {(a, 3), (e, 1)}
e.adj = {(b, 2), (d, 1)}
f.adj = {(b, 1), (c, 7), (g, 2)}
g.adj = {(c, 5), (f, 2), (h, 1)}
h.adj = {(g, 1)}

V = [a, b, c, d, e, f, g, h]
Dijkstra(a, V)

# fill V again since Dijkstra emptied it
V = [a, b, c, d, e, f, g, h]
print_shortest_paths(V)
