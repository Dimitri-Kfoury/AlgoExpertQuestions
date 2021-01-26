def maxProfitWithKTransactions(prices, k):
    profits = [[0 for j in range(len(prices))] for i in range(k + 1)]
    for i in range(1, k + 1):
        maxThusFar = float('-inf')
        for j in range(1, len(prices)):
            maxThusFar = max(maxThusFar,profits[i - 1][j - 1] - prices[j-1])
            profits[i][j] = max(profits[i][j-1], maxThusFar + prices[j] )

    return profits[-1][-1]


prices = [5, 11, 3, 50, 60, 90]
k = 2

print(maxProfitWithKTransactions(prices,k))
