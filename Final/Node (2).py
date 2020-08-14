class Node:

    # constructor
    # without name param, printing an object would give back location instead of name
    def __init__(self, name=None, parent=None, dst=float('inf'), adj=[], start=None, end=None):
        self.name = name
        self.parent = parent
        self.dst = dst
        self.adj = adj

        # for DFS
        self.start = start
        self.end = end

   # def add_adj(self):