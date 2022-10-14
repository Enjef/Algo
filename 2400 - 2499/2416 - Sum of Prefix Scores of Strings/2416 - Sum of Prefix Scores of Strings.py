class Solution:
    # 75.55% 37.32%
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        class Trie:
            def __init__(self):
                self.chars = [None] * 26
                self.count = 0

        root = Trie()
        for word in words:
            node = root
            for char in word:
                el = ord(char) - 97
                if not node.chars[el]:
                    node.chars[el] = Trie()
                node = node.chars[el]
                node.count += 1
        res = []
        for word in words:
            cur = 0
            node = root
            for char in word:
                el = ord(char) - 97
                node = node.chars[el]
                cur += node.count
            res.append(cur)
        return res


class Solution_v2:
    # 29.61% 46.24% (64.55% 41.48%)
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        class Trie:
            def __init__(self):
                self.chars = defaultdict(Trie)
                self.count = 0

        root = Trie()
        for word in words:
            node = root
            for char in word:
                node = node.chars[char]
                node.count += 1
        res = []
        for word in words:
            cur = 0
            node = root
            for char in word:
                node = node.chars[char]
                cur += node.count
            res.append(cur)
        return res


class Solution_v3:
    # 27.86% 43.25% (87.76% 46.18%)
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        class Trie:
            def __init__(self):
                self.chars = defaultdict(Trie)
                self.count = 0

        root = Trie()
        for word in words:
            node = root
            for char in word:
                node = node.chars[char]
                node.count += 1
        res = []
        for word in words:
            cur = 0
            node = root
            for i, char in enumerate(word):
                node = node.chars[char]
                if node.count == 1:
                    cur += len(word)-i
                    break
                cur += node.count
            res.append(cur)
        return res


class Solution_best_memory:
    def sumPrefixScores_best_memory(self, words: List[str]) -> List[int]:
        n = len(words)
        w = []
        c = [0] * n
        r = [0] * n
        for i in range(n):
            w.append([words[i], i])
        w.sort()
        for i in range(1, n):
            while c[i] < min(len(w[i - 1][0]), len(w[i][0])) and w[i - 1][0][c[i]] == w[i][0][c[i]]:
                c[i] += 1
        for i in range(n):
            p = len(w[i][0])
            r[w[i][1]] += len(w[i][0])
            for j in range(i + 1, n):
                p = min(p, c[j])
                if not p:
                    break
                r[w[i][1]], r[w[j][1]] = r[w[i][1]] + p, r[w[j][1]] + p
        return r


class Solution_best_speed:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        self.res = [len(s) for s in words]
        self.words = list(enumerate(words))
        self.add_longest_comm_prefix(0, self.words)
        return self.res

    def add_longest_comm_prefix(self, start, words_):
        if len(words_) < 2:
            return
        words = sorted(words_, key=lambda i: i[1][start:])
        shortest = words[0][1]
        len_ = 0
        for i in range(start, len(shortest)):
            if words[-1][1][i] == shortest[i]:
                len_ += 1
            else:
                break
        if len_ != 0:
            for i, w in words:
                self.res[i] += len_*(len(words)-1)

        dct = {chr(a): [] for a in range(ord('a'), ord('z') + 1)}
        new_start = start + len_
        for i, word in words:
            if len(word) > new_start:
                dct[word[new_start]].append((i, word))
        for w in dct.values():
            self.add_longest_comm_prefix(new_start, w)


class Solution_2nd_best_memory:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        p = 31
        m = 1e9 + 7
        p_pow = [1] * 1001
        for i in range(1001):
            p_pow[i] = (p_pow[i - 1] * p) % m

        hashes = [1] * len(words)
        res = [0] * len(words)
        for i in range(1001):
            mp = collections.defaultdict(int)
            for j in range(len(words)):
                if len(words[j]) <= i:
                    continue
                hashes[j] = (hashes[j] + (ord(words[j][i]) -
                             ord('a') + 1) * p_pow[i]) % m
                mp[hashes[j]] += 1
            for j in range(len(words)):
                if len(words[j]) <= i:
                    continue
                res[j] += mp[hashes[j]]
        return res
