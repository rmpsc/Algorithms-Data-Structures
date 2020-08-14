# Romel Pascua
# 017167304
# CECS 328 Lab 8
# DFS
from Node import *

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

aa = Node('a')
bb = Node('b')
cc = Node('c')
dd = Node('d')
ee = Node('e')
ff = Node('f')

a.adj = {b, c, d}
b.adj = {d}
c.adj = {d}
d.adj = {e}
e.adj = {g}
f.adj = {e}
g.adj = {}

aa.adj = {bb, cc}
bb.adj = {cc, dd, ee}
cc.adj = {ee}
dd.adj = {ff}
ee.adj = {bb, dd}
ff.adj = {ee}


G1 = [a, b, c, d, e, f, g]
G2 = [aa, bb, cc, dd, ee, ff]


print("G1")
DFS(G1)
print("\nG2")
DFS(G2)
