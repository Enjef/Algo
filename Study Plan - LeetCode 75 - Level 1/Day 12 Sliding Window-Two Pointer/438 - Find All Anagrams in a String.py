class Solution:
    # 71.08% 79.47%
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        n, m = len(p), len(s)
        total = set(p+s)
        if n > m:
            return res
        win = dict(zip(total, [0]*len(total)))
        target = win.copy()
        for i, char in enumerate(p):
            target[char] += 1
            win[s[i]] += 1
        if win == target:
            res.append(0)
        for i in range(n, m):
            prev, new = s[i-n], s[i]
            win[new] += 1
            win[prev] -= 1
            if win == target:
                res.append(i-n+1)
        return res
