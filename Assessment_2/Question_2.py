def maxSubsequenceDotProduct(arrayOne, arrayTwo):
    products = [[float('-inf') for j in range(len(arrayOne))] for i in range(len(arrayTwo))]

    products[0][0] = arrayOne[0] * arrayTwo[0]

    for i in range(1, len(arrayTwo)):
        products[i][0] = max(products[i - 1][0], arrayTwo[i] * arrayOne[0])

    for j in range(1, len(arrayOne)):
        products[0][j] = max(products[0][j - 1], arrayTwo[0] * arrayOne[j])

    for i in range(1, len(arrayTwo)):
        for j in range(1,len(arrayOne)):
            products[i][j] = max(arrayTwo[i] * arrayOne[j], products[i - 1][j - 1],
                                 products[i - 1][j - 1] + arrayTwo[i] * arrayOne[j], products[i - 1][j],
                                 products[i][j - 1], )


    return products[-1][-1]




array_one = [4, 7, 9, -6, 6]

array_two = [5, 1, -1, -3, -2, -10]

print(maxSubsequenceDotProduct(array_one,array_two))