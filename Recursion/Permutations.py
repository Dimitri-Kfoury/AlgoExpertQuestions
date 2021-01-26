def getPermutations(array):
    permutations = []
    per(0, array, permutations)
    return permutations


def per(idx, array, permutations):
    if (idx == len(array) - 1):
        permutations.append(array[:])
    else:
        for j in range(idx, len(array)):
            swap(idx, j, array)
            per(idx + 1, array, permutations)
            swap(j, idx, array)


def swap(i, j, array):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
