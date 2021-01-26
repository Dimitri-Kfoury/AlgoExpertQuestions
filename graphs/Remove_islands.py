def removeIslands(matrix):
    visited_nodes = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]

    if len(matrix == 1) or len(matrix[0]) == 1:
        return matrix

    for i in range(0, len(matrix), len(matrix) - 1):
        for j in range(len(matrix[0])):
            remove_1s(i, j, matrix, visited_nodes)
    for j in range(0, len(matrix[0]), len(matrix[0]) - 1):
        for i in range(len(matrix)):
            remove_1s(i, j, matrix, visited_nodes)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if not visited_nodes[i][j]:
                matrix[i][j] = 0

    return matrix


def remove_1s(i, j, matrix, visited_nodes):

    if i >= len(matrix) or j >= len(matrix[0]) or i < 0 or j < 0 or visited_nodes[i][j]:
        return
    else:
        visited_nodes[i][j] = True
        if matrix[i][j] == 1:
            remove_1s(i - 1, j, matrix, visited_nodes)
            remove_1s(i, j + 1, matrix, visited_nodes)
            remove_1s(i + 1, j, matrix, visited_nodes)
            remove_1s(i, j - 1, matrix, visited_nodes)


matrix =  [[1]]

islands = removeIslands(matrix)

for i in range(len(islands)):
    print(islands[i])
