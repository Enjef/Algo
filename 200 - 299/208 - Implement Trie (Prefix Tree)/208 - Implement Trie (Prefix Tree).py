# 36.85% 18.08% (29.16% 18.94%)
class Trie:

    def __init__(self):
        self.chars = dict()
        self.end = False

    def insert(self, word: str) -> None:
        if not word:
            self.end = True
            return
        cur = word[0]
        if cur not in self.chars:
            self.chars[cur] = Trie()
        self.chars[cur].insert(word[1:])

    def search(self, word: str) -> bool:
        if not word:
            return self.end
        cur = word[0]
        if cur not in self.chars:
            return False
        return self.chars[cur].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        cur = prefix[0]
        if cur not in self.chars:
            return False
        return self.chars[cur].startsWith(prefix[1:])

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


class Trie_best_speed:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur:
                cur[letter] = {}
            cur = cur[letter]
        cur['*'] = ''

    def search(self, word: str) -> bool:
        cur = self.root
        for letter in word:
            if letter not in cur:
                return False
            cur = cur[letter]
        return '*' in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for letter in prefix:
            if letter not in cur:
                return False
            cur = cur[letter]
        return True


class Trie_best_memory:
    def __init__(self):
        self.wordBank = []

    def insert(self, word: str) -> None:
        if word not in self.wordBank:
            self.wordBank.append(word)

    def search(self, word: str) -> bool:
        if word not in self.wordBank:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        for i in range(len(self.wordBank)):
            if len(self.wordBank[i]) >= len(prefix):
                if self.wordBank[i][:len(prefix)] == prefix:
                    return True
        return False
