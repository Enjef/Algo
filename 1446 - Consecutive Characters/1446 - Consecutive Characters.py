class Solution:
    def maxPower(self, s: str) -> int:  # 39.28% 89.47%
        out = 1
        cur = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1
            else:
                out = max(out, cur)
                cur = 1
        out = max(out, cur)
        return out

    def maxPower_best_speed(self, s: str) -> int:
        maxcount = count = 1
        char = s[0]
        for i in range(1, len(s)):
            if s[i] == char:
                count += 1
            else:
                char = s[i]
                if count > maxcount:
                    maxcount = count
                count = 1
        if count > maxcount:
            maxcount = count
        return maxcount
