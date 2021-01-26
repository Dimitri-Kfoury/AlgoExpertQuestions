def numberOfWaysToMakeChange(n, denoms):
    number_of_ways = [0 for i in range(n + 1)]
    number_of_ways[0] = 1
    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                number_of_ways[amount] += number_of_ways[amount - denom]


    return number_of_ways[n]


denoms = [1, 5, 10, 25]
n = 25
num = numberOfWaysToMakeChange(n, denoms)

print(num)
