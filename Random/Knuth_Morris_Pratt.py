
def knuthMorrisPrattAlgorithm(string, substring):
    patterns = find_patterns(substring)
    return match_strings(string,substring,patterns)
def find_patterns(string):
    i = 1
    j = 0
    patterns = [-1 for i in range(len(string))]

    while i < len(string):

        if string[i] == string[j]:
            patterns[i] = j
            j += 1
            i += 1
        elif j > 0:
            j = patterns[j - 1] + 1
        else:
            i += 1

    return patterns


def match_strings(string, substring, patterns):
    i = 0
    j = 0

    while i + len(substring) - j <= len(string):
        if string[i] == substring[j]:
            if j == len(substring) - 1:
                return True
            i += 1
            j += 1
        elif j > 0:
            j = patterns[j - 1] + 1
        else:
            i += 1
    return False
