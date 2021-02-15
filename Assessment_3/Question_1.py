def wordsInPhoneNumber(phoneNumber, words):
    key_pad = {'0': '0', '1': '1', 'a':'2','b':'2','c':'2','d':'3','e':'3','f':'3','g':'4','h':'4','i':'4', 'j': '5','k': '5','l': '5', 'm': '6','n': '6','o': '6',\
               'p':'7','q':'7','r':'7','s':'7','t':'8','u':'8','v':'8','w':'9','x':'9','y':'9','z':'9'}
    final_array = set()
    trie = Trie()
    word_mappings = populate_trie(trie,key_pad, words)

    for i in range(len(phoneNumber)):
        for j in range(len(phoneNumber)):
            word = phoneNumber[i:j+1]
            if trie.__contains__(word):
                for mapping in word_mappings[word]:
                    final_array.add(mapping)
    return list(final_array)

def populate_trie(trie,key_pad, words):
    words_mappings = {}
    for word in words:
        new_word = ''
        for char in word:
            new_word += (key_pad[char])
        if new_word not in words_mappings:
            words_mappings[new_word] = [word]
        else:
            words_mappings[new_word].append(word)
    for word in words_mappings.keys():
        trie.insert(word)
    return words_mappings



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

    def __contains__(self, item):
        current_trie = self.root
        for char in item:
            if char not in current_trie:
                return False
            current_trie = current_trie[char]
        return '*' in current_trie



