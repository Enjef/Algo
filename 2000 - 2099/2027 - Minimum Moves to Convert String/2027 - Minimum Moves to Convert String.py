class Solution:
    def minimumMoves(self, s: str) -> int:  # 5.34% 48.87%
        out = 0
        i = 0
        while i < len(s):
            if s[i] == 'X':
                out += 1
                i += 3
                continue
            i+= 1
        return out

    def minimumMoves_best_speed(self, s: str) -> int:
        i, count = 0, 0
        while i < len(s):
            if s[i] == 'X':
                count += 1
                i = i+3
            else:
                i += 1
        return count
