class Solution:
    def printVertically(self, s: str) -> List[str]:  # 87.21% 28.31%
        s = s.split()
        longest_word_len = len(max(s, key=len))
        out = ['']*longest_word_len
        for i in range(longest_word_len):
            for j in range(len(s)):
                out[i] += (
                    s[j][i] if i <= len(s[j])-1 or
                    len(s[j]) == longest_word_len else ' ')
        return [word.rstrip() for word in out]

    def printVertically_best_speed(self, s: str) -> List[str]:
        words = s.split()
        maxlen = max(map(len, words))
        def fulfill(x):
            nonlocal maxlen
            return x + ' '*(maxlen-len(x))
        res = []
        for c in zip(*map(fulfill, words)):
            res.append(''.join(c).rstrip())
        return res

    def printVertically_best_memory(self, s: str) -> List[str]:
        words = s.split()
        res = []
        max_length = 0
        for word in words:
            max_length = max(max_length, len(word))
        for i in range(max_length):
            vertical = ''
            for word in words:
                if i < len(word):
                    vertical += word[i]
                else:
                    vertical += ' '
            res.append(vertical.rstrip())
        return res

    def printVertically_2nd_best_memory(self, s: str) -> List[str]:
        return [
            ''.join(a).rstrip() for a in
            itertools.zip_longest(*s.split(), fillvalue=' ')
        ]
