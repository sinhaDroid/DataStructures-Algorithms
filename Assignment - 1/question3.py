

# function to add an edge to graph


def addEdge(u, v, w, graph):
    graph.append([u, v, w])

# A utility function to find set of an element i
# (uses path compression technique)


def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

# A function that does union of two sets of x and y
# (uses union by rank)


def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    # Attach smaller rank tree under root of
    # high rank tree (Union by Rank)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot

    # If ranks are same, then make one as root
    # and increment its rank by one
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

# The main function to construct MST using Kruskal's algorithm


def KruskalMST(graph, vertices, int_vertices):

    result = []  # This will store the resultant MST

    i = 0  # An index variable, used for sorted edges
    e = 0  # An index variable, used for result[]

    # Step 1:  Sort all the edges in non-decreasing
    # order of their
    # weight.  If we are not allowed to change the
    # given graph, we can create a copy of graph
    graph = sorted(graph, key=lambda item: item[2])

    parent, rank = [], []

    # Create vertices subsets with single elements
    for node in range(vertices):
        parent.append(node)
        rank.append(0)

    # Number of edges to be taken is equal to vertices-1
    while e < vertices - 1:

        # Step 2: Pick the smallest edge and increment
        # the index for next iteration
        u, v, w = graph[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)

        # If including this edge does't cause cycle,
        # include it in result and increment the index
        # of result for next edge
        if x != y:
            e = e + 1
            result.append([u, v, w])
            # Include reverse edge and value
            result.append([v, u, w])
            union(parent, rank, x, y)
        # Else discard the edge

    # print the contents of result[] to display the built MST
    # and append in final_result

    temp = []
    final_result = {}

    print("Following are the edges in the constructed MST")
    for u, v, weight in result:
        # print str(u) + " -- " + str(v) + " == " + str(weight)
        u = int_vertices[u]
        v = int_vertices[v]
        # print("%c -- %c == %d" % (u, v, weight))
        temp = (v, weight)

        if u not in final_result:
            final_result[u] = [temp]
        else:
            final_result[u].append(temp)

    return final_result


def question3(G):

    # G should have more than one node
    if len(G) < 2:
        return "G doesn't have enough vertices to form edges"

    # initialize a graph array
    graph = []

    # assign each string vertices to int vertices
    temp_vertices = {}
    int_vertices = {}
    count = 0

    # keys in vertices
    vertices = G.keys()

    for i in vertices:
        temp_vertices[i] = count
        int_vertices[count] = i
        count += 1

    for vertice in vertices:
        for edge in G[vertice]:
            addEdge(temp_vertices[vertice],
                    temp_vertices[edge[0]], edge[1], graph)

    return KruskalMST(graph, count, int_vertices)


G = {'A': [('B', 2)],
     'B': [('A', 2), ('C', 5)],
     'C': [('B', 5)]}

# G = {'A': [('B', 7), ('D', 5)],
#      'B': [('A', 7), ('C', 8), ('D', 9), ('E', 7)],
#      'C': [('B', 8), ('E', 5)],
#      'D': [('A', 5), ('B', 9), ('E', 15), ('F', 6)],
#      'E': [('B', 7), ('C', 5), ('D', 15), ('F', 8), ('G', 9)],
#      'F': [('D', 6), ('E', 8), ('G', 11)],
#      'G': [('E', 9), ('F', 11)]}

H = {'A': [('D', 5), ('B', 7)],
     'B': [('A', 7), ('E', 7)],
     'C': [('E', 5)],
     'D': [('A', 5), ('F', 6)],
     'E': [('C', 5), ('B', 7), ('G', 9)],
     'F': [('D', 6)],
     'G': [('E', 9)]}

print(question3(G))
