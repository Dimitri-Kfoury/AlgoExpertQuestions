def numbersInPi(pi, numbers):
    numbers_table = {}

    for number in numbers:
        numbers_table[number] = number
    cache = [None for i in range(len(pi) + 1)]
    result = min_num(pi, numbers_table, cache, 0)
    if result is not None:
        return result
    else:
        return -1


def min_num(digits, numbers_table, cache, i):
    if digits == '':
        return -1

    if cache[i] is not None:
        return cache[i]

    nums = []

    for i in range(1, len(digits) + 1):
        if digits[0:i] in numbers_table.keys():
            suffix_min = min_num(digits[i:len(digits)], numbers_table, cache, i)
            if suffix_min is not None:
                if cache[i] is None:
                    cache[i] = suffix_min
                nums.append(1 + suffix_min)

    if nums != []:
        return min(nums)
    else:
        return None


pi = "3141592653589793238462643383279"
numbers = [
    "314159265358979323846",
    "26433",
    "8",
    "3279",
    "314159265",
    "35897932384626433832",
    "79"
]
print(pi[len(pi):len(pi)] == '')
print(numbersInPi(pi, numbers))
