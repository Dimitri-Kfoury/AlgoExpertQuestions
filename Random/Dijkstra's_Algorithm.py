def dijkstrasAlgorithm(start, edges):
    visited_nodes = set()

    shortest_paths = [float('inf') for i in range(len(edges))]

    shortest_paths[start] = 0

    while len(visited_nodes) != len(edges):

        current_node = get_next_node(shortest_paths, visited_nodes)
        print(current_node)
        if current_node == -1 or shortest_paths[current_node] == float('inf'):
            break

        visited_nodes.add(current_node)

        for edge in edges[current_node]:
            if edge[0] not in visited_nodes and shortest_paths[current_node] + edge[1] <= shortest_paths[edge[0]]:
                shortest_paths[edge[0]] = shortest_paths[current_node] + edge[1]
    return shortest_paths

def get_next_node(shortest_paths, visited):
    min_distance = float('inf')
    next_node = -1

    for i in range(len(shortest_paths)):
        if i not in visited and shortest_paths[i] <= min_distance:
            min_distance = shortest_paths[i]
            next_node = i


    return next_node


edges = [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []]
start = 0
print(dijkstrasAlgorithm(start,edges))