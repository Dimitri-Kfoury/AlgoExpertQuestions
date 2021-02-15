def repeatedMatrixValues(matrix):


    previous_set = set()
    current_set = set()

    n = len(matrix[0])
    m = len(matrix)

    for k in range(n):
        previous_set.add(matrix[0][k])

    for i in range(1,m):
        for j in range(n):
            if matrix[i][j] in previous_set:
                current_set.add(matrix[i][j])
        previous_set = current_set
        current_set = set ()

    for j in range(n):
        for i in range(m):
            if matrix[i][j] in previous_set:
                current_set.add(matrix[i][j])
        previous_set = current_set
        current_set = set()


    return list(previous_set)


matrix = [[1, 3, 7, 4, 5],
    [2, 5, 9, 3, 3],
    [1, 8, 5, 3, 5],
    [5, 0, 3, 5, 6],
    [3, 8, 3, 5, 6],
    [1, 0, 3, 0, 5]
  ]

print(repeatedMatrixValues(matrix))