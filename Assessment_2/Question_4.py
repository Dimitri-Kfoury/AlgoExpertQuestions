def spinRings(array):
    upper_row = 0
    left_col = 0
    lower_row = len(array) - 1
    right_col = len(array[0]) - 1

    while upper_row < lower_row and left_col < right_col:
        rotate_ring(upper_row, left_col, lower_row, right_col, array)
        upper_row += 1
        lower_row -= 1
        left_col += 1
        right_col -= 1

    pass


def rotate_ring(upper_row, left_col, lower_row, right_col, array):
    temp_1 = array[upper_row][left_col]

    for j in range(left_col + 1, right_col + 1):
        temp_2 = array[upper_row][j]
        array[upper_row][j] = temp_1
        temp_1 = temp_2

    for i in range(upper_row + 1, lower_row + 1):
        temp_2 = array[i][right_col]
        array[i][right_col] = temp_1
        temp_1 = temp_2

    for j in range(right_col - 1, left_col - 1, -1):
        temp_2 = array[lower_row][j]
        array[lower_row][j] = temp_1
        temp_1 = temp_2

    for i in range(lower_row - 1, upper_row - 1, -1):
        temp_2 = array[i][left_col]
        array[i][left_col] = temp_1
        temp_1 = temp_2


array = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

spinRings(array)

for row in array:
    print(row)
