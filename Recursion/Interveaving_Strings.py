def interweavingStrings(one, two, three):
    if len(three) != len(one) + len(two):
        return False
    cache = [[None for j in range(len(two) + 1)] for i in range(len(one) + 1)]

    return inter(0, 0, one, two, three, cache)

def inter(i, j, one, two, three, cache):
    k = i + j

    if cache[i][j] is not None:
        return cache[i][j]

    if k == len(three):
        return True

    if i < len(one):
        cache[i][j] = inter(i + 1, j, one, two, three, cache)
        if cache[i][j]:
            return True

    if j < len(two):
        cache[i][j] = inter(i, j + 1, one, two, three, cache)
        return cache[i][j]
    cache[i][j] = False
    return False


one = "algoexpert"
two = "your-dream-job"
three = "your-algodream-expertjob"

print(interweavingStrings(one, two, three))
