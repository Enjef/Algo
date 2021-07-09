class Solution:
    def balancedStringSplit(self, s: str) -> int:
        out = 0
        count = 0
        for i in range(len(s)):
            if s[i] == 'L':
                count += 1
            else:
                count -= 1
            if count == 0:
                out += 1
        return out
