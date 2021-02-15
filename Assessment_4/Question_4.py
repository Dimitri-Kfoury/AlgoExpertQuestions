def longestIncreasingMatrixPath(matrix):
    return max_path(1, 2, matrix, float('-inf'), visited_nodes=[[False for j in range(len(matrix[0]))] for i in range(len(matrix))])



def max_path(i, j, matrix, previous_value, visited_nodes):
    if i >= len(matrix) or i < 0 or j >= len(matrix[0]) or j < 0 or visited_nodes[i][j]:
        return 0

    current_value = matrix[i][j]


    if current_value <= previous_value:
        return 0

    else:
        visited_nodes[i][j] = True

        current_visited_nodes = visited_nodes

        up = 1 + max_path(i - 1, j, matrix, current_value, current_visited_nodes)
        current_visited_nodes = visited_nodes
        right = 1 + max_path(i, j + 1, matrix, current_value, current_visited_nodes)
        current_visited_nodes = visited_nodes
        down = 1 + max_path(i + 1, j, matrix,current_value, current_visited_nodes)
        current_visited_nodes = visited_nodes
        left = 1 + max_path(i, j - 1, matrix, current_value, current_visited_nodes)

        visited_nodes[i][j] = False



        return max(up,right,left,down)


