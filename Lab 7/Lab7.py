# Romel Pascua
# 017167304
# CECS 328 Lab 7
# BFS & Is_bipartite
from Node import *

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')

# Part A
a.adj = {c, d}
b.adj = {c, e}
c.adj = {a, b, d}
d.adj = {a, c, e, f}
e.adj = {b, d, f}
f.adj = {d, e, h}
g.adj = {}
h.adj = {f}

print("Part A")
vertex = input("What would you like your starting vertex to be? ")

# eval finds object that has same name as vertex string
BFS(eval(vertex))


# Part B
a.adj = {d}
b.adj = {d, f}
c.adj = {d, e}
d.adj = {a, b, c}
e.adj = {c}
f.adj = {b}
g.adj = {h, i}
h.adj = {g, i}
i.adj = {g, h}

print("\nPart B")
graph = [a, b, c, d, e, f, g, h, i]
Explore(graph)
for vertex in graph:
    print(vertex.name + " = " + vertex.color)
