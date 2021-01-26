def palindromePartitioningMinCuts(string):
    global i
    palindromicities = [[True for j in range(len(string))] for i in range(len(string))]

    for i in range(1, len(string) - 1):
        for j in range(i + 1):
            if string[i] != string[j] or not palindromicities[i - 1][j + 1]:
                palindromicities[i][j] = False
    for j in range(len(string) - 1):
        if string[len(string) - 1] != string[j] or not palindromicities[len(string) - 2][j + 1]:
            palindromicities[len(string) - 1][j] = False

    min_cuts = [float('-inf') for i in string]
    for i in range(len(string)):
        if palindromicities[i][0]:
            min_cuts[i] =0
        else:
            min_cuts[i] = min_cuts[i-1]+1
            for j in range(1,i):
                if palindromicities[i][j] and min_cuts[j-1] + 1 < min_cuts[i]:
                    min_cuts[i] = min_cuts[j-1] +1
    return min_cuts[-1]


string = 'ababbbabbababa'
string1 = 'abba'
print(palindromePartitioningMinCuts(string))
