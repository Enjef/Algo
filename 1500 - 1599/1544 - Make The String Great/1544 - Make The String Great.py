class Solution:
    def makeGood(self, s: str) -> str:  # 65.62% 14.14%
        for i in range(1, len(s)):
            if s[i] == s[i-1].swapcase():
                s = ''.join([s[:i-1], s[i+1:]])
                return self.makeGood(s)
        return s

    def makeGood_best_speed(self, s: str) -> str:
        res = []
        for c in s:
            if not res:
                res.append(c)
            elif res[-1].isupper() and res[-1].lower() == c:
                res.pop()
            elif res[-1].islower() and res[-1].upper() == c:
                res.pop()
            else:
                res.append(c)
        return ''.join(res)

    def makeGood_best_refactored_swapcase(self, s: str) -> str:  # 65.62% 14%
        res = []
        for char in s:
            if not res:
                res.append(char)
            elif res[-1].swapcase() == char:
                res.pop()
            else:
                res.append(char)
        return ''.join(res)
