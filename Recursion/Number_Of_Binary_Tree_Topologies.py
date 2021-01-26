def numberOfBinaryTreeTopologies1(n):
    cache = [1]

    for i in range(1, n + 1):
        sum = 0
        for j in range(i):
            left = cache[j]
            right = cache[i - 1 - j]
            sum += left * right
        cache.append(sum)
    return cache[n]


def numberOfBinaryTreeTopologies(n):
    if n == 0:
        return 1
    sum = 0
    for i in range(n):
        left = i
        right = n - 1 - i
        sum += numberOfBinaryTreeTopologies(left) * numberOfBinaryTreeTopologies(right)
    return sum


print(numberOfBinaryTreeTopologies1(10))
