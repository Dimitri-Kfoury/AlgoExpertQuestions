def powerSet(array):
    subsets = [[]]
    for element in array:
        for i in range(len(subsets)):
            subsets.append(subsets[i] + [element])
    return subsets



