import Heaps.Heap


def aStarAlgorithm(startRow, startCol, endRow, endCol, graph):
    open_set = Heaps.Heap.Heap([], comparison_func)

    nodes = initialize_nodes(graph)

    start_node = nodes[startRow][startCol]
    start_node.g_factor = 0
    end_node = nodes[endRow][endCol]

    open_set.insert(start_node)

    while not open_set.is_empty():
        current_node = open_set.remove()

        if current_node == end_node:
            return retrace_shortest_path(current_node,nodes)

        else:
            add_neighbors(current_node, nodes, open_set, end_node)
    return []


def manhattan_distance(node, end_node):
    return abs(node.row - end_node.row) + abs(node.col - end_node.col)


def comparison_func(node1, node2):
    f_factor_1 = node1.g_factor + node1.h_factor
    f_factor_2 = node2.g_factor + node2.h_factor

    return f_factor_1 < f_factor_2


class Node:
    def __init__(self, row, col, value):
        self.value = value
        self.id = str(row) + '-' + str(col)
        self.row = row
        self.col = col
        self.g_factor = float('inf')
        self.h_factor = float('inf')
        self.came_from = None


def initialize_nodes(graph):
    nodes = []

    for i in range(len(graph)):
        nodes.append([])
        for j in range(len(graph[0])):
            nodes[i].append(Node(i, j, graph[i][j]))
    return nodes


def add_neighbors(node, nodes, open_set, end_node):
    num_of_cols = len(nodes[0])
    num_of_rows = len(nodes)
    current_row = node.row
    current_col = node.col

    if current_row + 1 < num_of_rows and node.g_factor + 1 < nodes[current_row + 1][current_col].g_factor and \
            nodes[current_row + 1][current_col].value == 0:
        neighbor_node = nodes[current_row + 1][current_col]
        neighbor_node.g_factor = node.g_factor + 1
        neighbor_node.h_factor = manhattan_distance(neighbor_node, end_node)
        neighbor_node.came_from = node
        open_set.insert(neighbor_node)

    if current_col - 1 >= 0 and node.g_factor + 1 < nodes[current_row][current_col - 1].g_factor and nodes[current_row][
        current_col - 1].value == 0:
        neighbor_node = nodes[current_row][current_col - 1]
        neighbor_node.g_factor = node.g_factor + 1
        neighbor_node.h_factor = manhattan_distance(neighbor_node, end_node)
        neighbor_node.came_from = node
        open_set.insert(neighbor_node)

    if current_row - 1 >= 0 and node.g_factor + 1 < nodes[current_row - 1][current_col].g_factor and \
            nodes[current_row - 1][current_col].value == 0:
        neighbor_node = nodes[current_row - 1][current_col]
        neighbor_node.g_factor = node.g_factor + 1
        neighbor_node.h_factor = manhattan_distance(neighbor_node, end_node)
        neighbor_node.came_from = node
        open_set.insert(neighbor_node)

    if current_col + 1 < num_of_cols and node.g_factor + 1 < nodes[current_row][current_col + 1].g_factor and \
            nodes[current_row][current_col + 1].value == 0:
        neighbor_node = nodes[current_row][current_col + 1]
        neighbor_node.g_factor = node.g_factor + 1
        neighbor_node.h_factor = manhattan_distance(neighbor_node, end_node)
        neighbor_node.came_from = node
        open_set.insert(neighbor_node)


def retrace_shortest_path(end_node, nodes):
    current_node = end_node
    path = []

    while current_node is not None:
        path.append([current_node.row, current_node.col])
        current_node = current_node.came_from
    return list(reversed(path))


graph = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

print(aStarAlgorithm(0,1,4,3,graph))