def isSquare(precomputed_values, r1, r2, c1, c2):
    length = r2 - r1 + 1
    top = precomputed_values[r1][c1][0] >= length
    left = precomputed_values[r1][c1][1] >= length
    bottom = precomputed_values[r2][c1][0] >= length
    right = precomputed_values[r1][c2][1] >= length
    return top and left and bottom and right


def squareOfZeroes(matrix):
    precomputed_values = [[[0, 0] for n in range(len(matrix))] for n in range(len(matrix))]

    if matrix[len(matrix) - 1][len(matrix) - 1] == 1:
        precomputed_values[len(matrix) - 1][len(matrix) - 1][0] = precomputed_values[len(matrix) - 1][len(matrix) - 1][
            1] = 0
    else:
        precomputed_values[len(matrix) - 1][len(matrix) - 1][0] = precomputed_values[len(matrix) - 1][len(matrix) - 1][
            1] = 1

    for j in range(len(matrix) - 2, -1, -1):
        if matrix[len(matrix) - 1][j] == 1:
            precomputed_values[len(matrix) - 1][j][0] = 0
        else:
            precomputed_values[len(matrix) - 1][j][0] = precomputed_values[len(matrix) - 1][j + 1][0] + 1
            precomputed_values[len(matrix) - 1][j][1] = 1

    for i in range(len(matrix) - 2, -1, -1):
        if matrix[i][len(matrix) - 1] == 1:
            precomputed_values[i][len(matrix) - 1][1] = 0
        else:
            precomputed_values[i][len(matrix) - 1][1] = precomputed_values[i + 1][len(matrix) - 1][1] + 1
            precomputed_values[i][len(matrix) - 1][0] = 1

    for i in range(len(matrix) - 2, -1, -1):
        for j in range(len(matrix) - 2, -1, -1):

            if matrix[i][j] == 1:
                precomputed_values[i][j][0] = 0
                precomputed_values[i][j][1] = 0
            else:
                precomputed_values[i][j][0] = precomputed_values[i][j + 1][0] + 1
                precomputed_values[i][j][1] = precomputed_values[i + 1][j][1] + 1

    print(precomputed_values)
    n = len(matrix)
    for topRow in range(n):
        for leftCol in range(n):
            square_length = 2
            while square_length <= n - leftCol and square_length <= n - topRow:
                bottom_row = topRow + square_length - 1
                rightCol = leftCol + square_length - 1
                if isSquare(precomputed_values, topRow, bottom_row, leftCol, rightCol):
                    return True
                square_length += 1
    return False


matrix = [[0, 0],[0, 0]]
print(squareOfZeroes(matrix))
