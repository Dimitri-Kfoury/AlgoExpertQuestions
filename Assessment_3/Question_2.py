def balanceIndex(array):

    sum_right = 0
    sum_left = sum(array[1:])
    if sum_left == 0:
        return 0
    for i in range(1,len(array)):
        sum_right += array[i-1]
        sum_left-= array[i]
        if sum_left == sum_right:
            return i

    return -1







array = [0,9,-8,2,7,1,11,-2,1]

print(balanceIndex(array))
