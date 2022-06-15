class Solution:
    def longestStrChain(self, words: List[str]) -> int:  # 5.01% 48.74%
        def check(one, two):
            for i in range(len(two)):
                if two[:i]+two[i+1:] == one:
                    return True
            return False

        d = defaultdict(set)
        res = 1
        start, end = float('inf'), 0
        for word in words:
            n = len(word)
            d[n].add((word, 1))
            start = min(start, n)
            end = max(end, n)
        stack = d[start]
        for i in range(start, end):
            new = set()
            for parent, level in stack:
                for child in d[i+1]:
                    if check(parent, child[0]):
                        new.add((child[0], level+1))
                        res = max(res, level+1)
            stack = new
            stack.update(d[i+1])
        return res

    def longestStrChain_best_speed(self, words: List[str]) -> int:
        seenWords = {word: 1 for word in words}
        words.sort(key=lambda x: len(x))
        longest = 0
        for w in words:
            for i in range(len(w)):
                tmpW = w[:i] + w[i+1:]
                if tmpW in seenWords:
                    seenWords[w] = max(seenWords[w], 1 + seenWords[tmpW])
            longest = max(longest, seenWords[w])
        return longest

    def longestStrChain_2nd_best_speed(self, words: List[str]) -> int:
        self.wordsPresent = set(words)
        self.memo = {}
        reply = 0

        def dfs(word):
            if word in self.memo:
                return self.memo[word]
            maxLength = 1
            tmp = list(word)
            for i in range(len(word)):
                tmp.pop(i)
                a2s = ''.join(tmp)
                if a2s in self.wordsPresent:
                    length = 1 + dfs(a2s)
                    maxLength = max(length, maxLength)
                tmp.insert(i, word[i])
            self.memo[word] = maxLength
            return maxLength
        words.sort(key=len)
        for word in words[::-1]:
            reply = max(reply, dfs(word))
            if reply == len(word) - len(words[0]) + 1:
                break
        return reply

    def longestStrChain_best_memory(self, words: List[str]) -> int:
        words = sorted(words, key=lambda x: len(x))
        dp = [1]*len(words)

        def check(w1, w2):
            i = j = 0
            count = 0
            while i < len(w1) and j < len(w2) and count < 2:
                if w1[i] == w2[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
                    count += 1
            return True if count < 2 else False

        for i in range(len(words)):
            j = i+1
            while j < len(words) and len(words[j]) <= len(words[i])+1:
                if len(words[j]) == len(words[i])+1 and check(words[i], words[j]):
                    dp[j] = max(dp[j], dp[i]+1)
                j += 1
        return max(dp)

    def longestStrChain_3d_best_memory(self, words: List[str]) -> int:
        def is_pred(a, b):
            if len(b) - len(a) != 1:
                return False
            for i in range(len(b)):
                if b[0:i] + b[i+1:] == a:
                    return True
            return False

        n = len(words)
        dp = [1] * n
        sort_words = sorted(words, key=len)
        for i in range(n):
            for j in range(i):
                if is_pred(sort_words[j], sort_words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
