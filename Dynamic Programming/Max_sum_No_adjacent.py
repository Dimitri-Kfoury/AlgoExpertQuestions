def maxSubsetSumNoAdjacent(array):

    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    
    max_sum1 = array[0]
    max_sum2 = array[1]
    sum = 0
    for i in range(2, len(array)):
        temp = max_sum2
        max_sum2 = max(max_sum1 + array[i], max_sum2)
        max_sum1 = max(max_sum1,temp)
    return max(max_sum1,max_sum2)

a = [75, 105, 120, 75, 90, 135]
print(maxSubsetSumNoAdjacent(a))