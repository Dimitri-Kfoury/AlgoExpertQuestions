def countContainedPermutations(bigString, smallString):
    trie = Trie()

    smallStrings = []
    permutation(trie, '', smallString, smallStrings)

    count = 0

    for i in range(len(bigString)):
        for j in range(i, len(bigString) + 1):
            current_string = bigString[i:j]
            if trie.__contains__(current_string):
                count += 1

    return count


class Trie:
    def __init__(self):
        self.root = {}

    def add_word(self, word):

        current_node = self.root

        for char in word:
            if char not in current_node:
                current_node[char] = {}
            current_node = current_node[char]
        current_node['*'] = word

    def __contains__(self, word):
        current_node = self.root

        for char in word:
            if char not in current_node:
                return False
            current_node = current_node[char]
        return '*' in current_node


def permutation(trie, prefix, str, permutations):
    n = len(str)
    if n == 0:
        permutations.append(prefix)
        trie.add_word(prefix)
    else:
        for i in range(n):
            permutation(prefix + str[i], str[0: i] + str[i + 1: n], permutations)


permutations = []

permutation('', 'abc', permutations)

print(permutations)
