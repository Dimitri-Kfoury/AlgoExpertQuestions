def minimumAreaRectangle(points):
    map = {}

    for point in points:
        map[(point[0], point[1])] = True

    min_area = float('inf')

    n = len(points)

    for i in range(n):
        p_1 = points[i]
        for j in range(i + 1,n):
           p_2 = points[j]
           if p_1[0] != p_2[0] and p_1[1] != p_2[1] and (p_2[0],p_1[1]) in map and (p_1[0],p_2[1]) in map:
               current_area = abs(p_1[0] - p_2[0]) * abs(p_1[1] - p_2[1])
               if current_area < min_area:
                   min_area = current_area

    return min_area


points = [
    [1, 5],
    [5, 1],
    [4, 2],
    [2, 4],
    [2, 2],
    [1, 2],
    [4, 5],
    [2, 5],
    [-1, -2]
]



print(minimumAreaRectangle(points))