def globMatching(fileName, pattern):
    table = [[False for j in range(len(fileName) + 1)] for i in range(len(pattern) + 1)]
    table[0][0] = True

    for i in range(1, len(pattern) + 1):
        table[i][0] = table[i - 1][0] if pattern[i - 1] == '*' else False
    for i in range(1, len(pattern) + 1):
        for j in range(1, len(fileName) + 1):
            if pattern[i - 1] == '*':
                table[i][j] = table[i - 1][j - 1] or table[i - 1][j] or table[i][j - 1]
            elif pattern[i - 1] == '?':
                table[i][j] = table[i - 1][j - 1]
            else:
                if pattern[i - 1] != fileName[j - 1]:
                    table[i][j] = False
                else:
                    table[i][j] = table[i - 1][j - 1]
    return table[-1][-1]


table = globMatching('affdeg', '*****a*?f*********g')

print(table)
