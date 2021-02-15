def multiStringSearch(bigString, smallStrings):
    trie = Trie()

    for string in smallStrings:
        trie.add_word(string)
    strings_found = {}

    for i in range(len(bigString)):
        for j in range(i, len(bigString) +1):
            current_string = bigString[i:j]
            if trie.__contains__(current_string):
                strings_found[current_string] = True


    return [string in strings_found for string in smallStrings]


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


