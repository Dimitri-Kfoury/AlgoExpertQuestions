def minNumberOfJumps(array):
    min_jumps = [0 for x in range(len(array))]

    for i in range(1,len(array)):
        min_jumps[i] = min_jumps[i-1] +1
        for j in range(i):
            if array[j] + j >= i and min_jumps[j] + 1 < min_jumps[i]:
                min_jumps[i] = min_jumps[j] +1

    return min_jumps


def minNumberOfJumps1(array):
    if len(array) <= 1:
        return 0
    maxReach = array[0]
    steps = array[0]
    jumps = 1
    for i in range(1,len(array) -1):
        maxReach = max(maxReach,i + array[i])
        print(maxReach)
        steps-=1
        if steps == 0:
            jumps+=1
            steps = maxReach - i
    return jumps





