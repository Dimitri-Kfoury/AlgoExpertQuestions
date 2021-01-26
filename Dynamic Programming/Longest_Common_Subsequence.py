def longestCommonSubsequence(str1, str2):
    lcs = [[[] for x in range(len(str2) + 1)] for y in range(len(str1) + 1)]

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + [str2[j - 1]]
            else:
                lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j], key=len)
    return lcs[-1][-1]


def longestCommonSubsequence1(str1, str2):
    return l(str1, str2)


def l(str1, str2):
    if str1 == '' or str2 == '':
        return []
    if str1[len(str1) - 1] == str2[len(str2) - 1]:
        return l(str1[0:len(str1) - 1], str2[0:len(str2) - 1]) + [str1[len(str1) - 1]]
    else:
        return max(l(str1[0:len(str1) - 1], str2), l(str1, str2[0:len(str2) - 1]), key=len)



def longestCommonSubsequence2(str1, str2):
    lcs = [[0 for x in range(len(str2) + 1)] for y in range(len(str1) + 1)]

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])
    return construct_sequence(lcs,str1)

def construct_sequence(lcs,str1):
    i = len(lcs) -1
    j = len(lcs[0]) -1
    result = []
    while i!=0 and j!=0:
        if lcs[i][j] == lcs[i-1][j]:
            i-=1
        elif lcs[i][j] == lcs[i][j-1]:
            j-=1
        else:
            result.append(str1[i-1])
            i-=1
            j-=1
    return list(reversed(result))




str1 = "ABCCDCEFEE"
str2 = "CCCEEEF"

print(longestCommonSubsequence2(str1,str2))