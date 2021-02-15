def kadanesAlgorithm(array):
    max_sums = [0 for i in range(len(array))]

    max_sums[0] = array[0]
    max_so_far = array[0]

    for i in range(1, len(array)):
        max_sums[i] = max(max_sums[i - 1] + array[i], array[i])
        max_so_far = max(max_so_far, max_sums[i])
    return max_so_far


