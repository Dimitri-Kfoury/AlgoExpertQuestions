def waterArea(heights):

    if len(heights) < 1:
        return 0

    left_and_right_max = [[0, 0] for i in range(len(heights))]

    left_max = heights[0]
    for i in range(len(heights)-1):
        left_and_right_max[i][0] = left_max
        left_max = max(left_max, heights[i])

    right_max = heights[len(heights) - 1]
    for i in range(len(heights) - 2, 0, -1):
        left_and_right_max[i][1] = right_max
        right_max = max(right_max, heights[i])

    water_above = []
    for i in range(len(heights)):
        water = min(left_and_right_max[i][0],left_and_right_max[i][1]) - heights[i]
        if water > 0:
            water_above.append(water)
        else:
            water_above.append(0)
    return sum(water_above)



left_and = waterArea(heights=[0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3])
print(left_and)
