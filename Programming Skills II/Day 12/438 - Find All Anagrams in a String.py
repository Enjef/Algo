class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:  # 63.62% 6.64%
        res = []
        n, m = len(p), len(s)
        if n > m:
            return res
        win = dict(zip(set(p), [0]*len(set(p))))
        target = dict(zip(set(p), [0]*len(set(p))))
        diff = 0
        for i in range(n):
            target[p[i]] += 1
            if s[i] in win:
                win[s[i]] += 1
            else:
                diff += 1
        for key in target:
            if win[key] != target[key]:
                diff += 1
        if diff == 0:
                res.append(0)
        for i in range(n, m):
            if s[i-n] in win:
                if win[s[i-n]] == target[s[i-n]]:
                    diff += 1
                win[s[i-n]] -= 1
                if win[s[i-n]] == target[s[i-n]]:
                    diff -= 1
            else:
                diff -= 1
            if s[i] in win:
                if win[s[i]] == target[s[i]]:
                    diff += 1
                win[s[i]] += 1
                if win[s[i]] == target[s[i]]:
                    diff -= 1
            else:
                diff += 1
            if diff == 0:
                res.append(i-n+1)
        return res

    def findAnagrams_v2(self, s: str, p: str) -> List[int]:  # 60.83% 38.21%
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
