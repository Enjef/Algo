class Solution:
    def replaceWords(
            self, dictionary: List[str], sentence: str) -> str:  # 55.08% 81.59%
        dictionary.sort()
        sentence = sentence.split()
        for i, word in enumerate(sentence):
            for test in dictionary:
                if word.startswith(test):
                    sentence[i] = test
                    break
        return ' '.join(sentence)

    def replaceWords_best_speed(self, dictionary, sentence):
        trie = {}
        for word in dictionary:
            cur = trie
            for char in word:
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            cur['#'] = '#'
        res = []
        for word in sentence.split(' '):
            cur = trie
            find = False
            for i, char in enumerate(word):
                if char not in cur:
                    break
                cur = cur[char]
                if '#' in cur:
                    res.append(word[:i+1])
                    find = True
                    break

            if not find:
                res.append(word)

        res = ' '.join(res)
        return res

    def replaceWords_best_memory(self, dictionary, sentence):
        dictionary = set(dictionary)
        l = sentence.split(' ')
        for idx, i in enumerate(l):
            temp = ''
            for j in i:
                temp = temp + j
                if temp in dictionary:
                    l[idx] = temp
                    break
        return ' '.join(l)


class Trie:
    def __init__(self, words):
        self.root = {}
        for word in words:
            self.add_word(word)

    def add_word(self, word):
        node = self.root
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node['*'] = {}

    def find_root(self, word):
        node = self.root
        for index, letter in enumerate(word):
            if letter not in node:
                return word
            node = node[letter]
            if '*' in node:
                return word[:index+1]
        return word


class Solution_3rd_best:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie(dictionary)
        return ' '.join(trie.find_root(word)
                        for word in sentence.split())
