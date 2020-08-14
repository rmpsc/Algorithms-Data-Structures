class Node:

    # constructor
    # without name param, printing an object would give back location instead of name
    def __init__(self, name=None, parent=None, adj=None, start=None, end=None):
        self.name = name
        self.parent = parent
        self.adj = adj
        self.start = start
        self.end = end


time = 0
topological = []
def DFS(V):
    global time
    global topological
    for v in V:
        if v.parent is None:
            v.parent = -1
            DFS_visit(v)
    for v in topological:
        for n in v.adj:
            if v.start > n.start and v.end < n.end:
                print("Cycle detected, topological sort is impossible")
                # prints first backward edge found (if any)
                print("backward edge at " + str(v.name) + "->" + str(n.name))
                exit()
    for v in topological:
        print(str(v.name) + " " + str(v.start) + "/" + str(v.end))


def DFS_visit(v):
    global time
    global topological
    topological.append(v)
    time += 1
    v.start = time
    for n in v.adj:
        if n.start is None:
            n.parent = v
            DFS_visit(n)
    time += 1
    v.end = time
