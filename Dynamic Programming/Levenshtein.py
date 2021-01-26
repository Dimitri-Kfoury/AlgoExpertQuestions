def minNumberOfCoinsForChange(n, denoms):
    amounts = [[0 for i in range(n + 1)] for j in range(len(denoms))]
    denoms.sort()
    for i in range(n+1):
        if denoms[0] > i:
            amounts[0][i] = 0
        else:
            if amounts[0][i - denoms[0]] > 0:
                amounts[0][i] = amounts[0][i - denoms[0]] + 1
            else:
                if denoms[0] == i:
                    amounts[0][i] = 1
                else:
                    amounts[0][i] = 0


    for i in range(1,len(denoms)):
        for j in range(1, n + 1):
            if denoms[i] > j:
                amounts[i][j] = amounts[i - 1][j]
            else:
                if amounts[i][j - denoms[i]] > 0:
                    amounts[i][j] = min(amounts[i][j - denoms[i]] + 1, amounts[i - 1][j])
                else:
                    if denoms[i] == j:
                        amounts[i][j] = 1
                    else:
                        amounts[i][j] = amounts[i - 1][j]
    return amounts

denoms = [3,5]
n = 9
print(minNumberOfCoinsForChange(n,denoms))