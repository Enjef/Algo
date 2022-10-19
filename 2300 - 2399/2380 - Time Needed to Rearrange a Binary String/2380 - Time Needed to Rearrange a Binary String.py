class Solution:
    # 78.54% 7.51% (84.87% 77.22%)
    def secondsToRemoveOccurrences(self, s: str) -> int:
        res = 0
        while '01' in s:
            s = s.replace('01', '10')
            res += 1
        return res


class Solution_best_speed:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        req = prefix = prev = 0
        for i, c in enumerate(s):
            if c == '1':
                req = max(prev, i-prefix)
                prefix += 1
                if req:
                    prev = req + 1
        return req
