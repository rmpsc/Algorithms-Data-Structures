from Node import *

def Cycle(a):
    print("\n" + str(a))

    # array of objects
    graph = []
    for i in a:
        first = i[0]
        last = i[-1]
        for x in graph:
            if x.name == first:
                break
        else:
            graph.append(Node(first))
            for x in graph:
                if x.name == last:
                    break
            else:
                graph.append(Node(last))

    '''
    # makes correct neighbors
    for v in final:
        for n in final:
            if v.name[-1] == n.name[0]:
                v.adj.append(n)
                print(str(v.name) + " and " + str(n.name) + " share " + str(v.name[-1]))
    '''

    for v in a:
        # print("\nv is " + v)
        for n in a:
            if v[-1] == n[0]:
                # print(v + " needs to add " + n)
                for x in graph:
                    if x.name == v[0]:
                        for y in graph:
                            if y.name == n[0]:
                                x.adj.append(y)

    DFS(graph)
    # checks if in_deg == out_deg and if only one parent is -1
    if in_n_out(graph) and parent_count(graph):
        print("CYCLE!")
    else:
        print("NOT A CYCLE!")

time = 0
topological = []
def DFS(V):
    global time
    global topological
    for v in V:
        if v.parent is None:
            v.parent = -1
            DFS_visit(v)

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


def in_n_out(V):
    in_deg = 0
    for v in V:
        # print("v is " + str(v.name))
        for n in V:
            # print("n is " + str(n.name))
            for j in n.adj:
                if j == v:
                    # print(str(j.name) + " = " + str(v.name))
                    in_deg += 1
        if in_deg != len(v.adj):
            # print("in_deg != out_deg")
            return False
        in_deg = 0
    return True


def parent_count(V):
    p_count = 0
    for node in V:
        if node.parent == -1:
            p_count += 1
    if p_count > 1:
        # print("more than 1 parent that = -1")
        return False
    else:
        return True
