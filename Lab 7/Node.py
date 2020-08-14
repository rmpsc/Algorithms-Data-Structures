class Node:

    # constructor
    # without name param, printing an object would give back location instead of name
    def __init__(self, name=None, parent=None, dst=None, adj=None, color=None):
        self.name = name
        self.parent = parent
        self.dst = dst
        self.adj = adj
        self.color = color


def BFS(s):
    fifo = [s]
    path = []
    s.parent = -1
    s.dst = 0
    while fifo:
        temp = fifo.pop(0)
        for node in temp.adj:
            # checks if node has been checked
            if node.parent is None:
                node.parent = temp
                node.dst = temp.dst + 1
                fifo.append(node)

                # stores path from end to start
                temp_path = node
                path.append(temp_path)

                # stops when it reaches the end
                while temp_path.parent is not -1:
                    path.append(temp_path.parent)
                    temp_path = temp_path.parent

                # adds the end
                path.append(s)

                # prints the path and distance
                print("path = ", end=" ")
                for i in path:
                    if i.parent == -1:
                        break
                    print(i.name, end=" ")
                print(s.name, end=" ")
                print(" dst = " + str(node.dst))
                path.clear()


def Explore(g):
    for node in g:
        node.color = "gray"
        # resets parents from part A
        node.parent = None
    for node in g:
        if node.color == "gray":
            node.color = "blue"
            bipartite = Is_bipartite(node)
            if bipartite == -1:
                print("NOT bipartite")


def Is_bipartite(node):
    Q = [node]
    node.parent = -1
    while Q:
        u = Q.pop(0)
        for v in u.adj:
            if v.color == u.color:
                return -1
            if v.parent is None:
                v.parent = u
                if v.color == "gray":
                    if u.color == "blue":
                        v.color = "red"
                    if u.color == "red":
                        v.color = "blue"
                Q.append(v)
