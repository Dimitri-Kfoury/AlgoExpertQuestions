def multiStringSearch(bigString, smallStrings):
    root = Trie()

    for smallString in smallStrings:
        root.insert(smallString)
    strings_found = {}

    for i in range(len(bigString)):
        helper(bigString,i,strings_found,root)
    return [string in strings_found for string in smallStrings]


class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def insert(self, string):

        current_trie = self.root
        for char in string:
            if char not in current_trie:
                current_trie[char] = {}
            current_trie = current_trie[char]
        current_trie[self.end_symbol] = string


def helper(big_string, start_idx, strings_found, trie):

    current_node =  trie.root

    for i in range(start_idx,len(big_string)):
        current_char = big_string[i]
        if current_char not in current_node:
            break
        current_node = current_node[current_char]
        if trie.end_symbol in current_node:
            strings_found[current_node[trie.end_symbol]] = True

