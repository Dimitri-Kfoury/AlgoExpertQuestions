
def cycleInGraph(edges):
    is_loop = False

    for edge in range(len(edges)):
        is_loop = is_loop or find_loop(edge,edges,visited_nodes={})

    return is_loop


def find_loop(edge,edges,visited_nodes):


    if edge in visited_nodes and visited_nodes[edge]:
        return True


    else:
        visited_nodes[edge] = True
        loop = False
        for child_edges in edges[edge]:
            loop  = loop or find_loop(child_edges,edges,visited_nodes)
            visited_nodes[child_edges] = False
    return loop


edges = [[1, 2], [2], []]

print(cycleInGraph(edges))