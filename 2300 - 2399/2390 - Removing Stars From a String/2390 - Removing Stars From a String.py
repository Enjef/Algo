class Solution:
    # 11.50% 80.99% (21.97% 93.35%)
    def removeStars(self, s: str) -> str:
        deletions = 0
        res = []
        for i in range(len(s)-1, -1, -1):
            if s[i] == '*':
                deletions += 1
            else:
                if not deletions:
                    res.append(s[i])
                    continue
                deletions -= 1
        return ''.join(res)[::-1]

    def removeStars_best_speed(self, s: str) -> str:
        res = []
        for i in s:
            if i != '*':
                res.append(i)
            else:
                res.pop()
        return ''.join(res)

    def removeStars_2nd_best_speed(self, s: str) -> str:
        l = []
        stars = 0
        for c in reversed(s):
            if c == '*':
                stars += 1
            elif stars:
                stars -= 1
            else:
                l.append(c)
        return ''.join(reversed(l))

    def removeStars_best_memory(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            if s[i] == '*' and res:
                l = len(res)
                res = res[0:l-1]
            elif s[i] != '*':
                res += s[i]
        return res
