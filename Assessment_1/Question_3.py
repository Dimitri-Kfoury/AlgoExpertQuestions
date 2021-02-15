def specialStrings(strings):
    trie = Trie()
    final_array = []

    for string in strings:
        trie.insert(string)

    for string in strings:
        if is_special(string, trie.root, trie, 0, 0):
            final_array.append(string)
    return final_array


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


def is_special(string, trie_node, idx, count, trie):
    char = string[idx]

    if idx == len(string) - 1:
        return char in trie_node and '*' in trie_node[char] and count + 1 >= 2

    else:
        if char in trie_node and '*' in trie_node[char]:
            rest_is_special = is_special(string[idx + 1:], trie.root, 0, count + 1, trie)
            if rest_is_special:
                return True
        elif char not in trie_node:
            return False
    return is_special(string, trie_node[char], idx + 1, count, trie)
