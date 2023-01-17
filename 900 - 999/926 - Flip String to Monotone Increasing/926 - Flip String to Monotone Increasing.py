class Solution:
    # 62.18% 45.83% (63.14% 45.83%)
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        right = s.count('0')
        result = min(s.count('1'), right)
        left = 0
        for i, char in enumerate(s):
            if char == '1':
                left += 1
            else:
                right -= 1
            result = min(result, left + right)
            if right == n-i-1:
                break
        return result

    # 72.76% 93.27% (71.15%  93.27%)
    def minFlipsMonoIncr_v2(self, s: str) -> int:
        n = len(s)
        right = s.count('0')
        result = min(s.count('1'), right)
        left = 0
        for i, char in enumerate(s):
            if char == '1':
                left += 1
            else:
                right -= 1
            result = min(result, left + right)
        return result


class Solution_best_speed:
    def minFlipsMonoIncr(self, s):
        min_diff = 0
        ones_count = 0
        for c in s:
            if c == '1':
                ones_count += 1
            elif ones_count > min_diff:
                min_diff += 1
        return min_diff


class Solution_best_memory:
    def minFlipsMonoIncr(self, s: str) -> int:
        zeros, ones = s.count('0'), 0
        res = zeros
        for digit in s:
            if digit == '0':
                zeros -= 1
            else:
                ones += 1
            res = min(res, zeros + ones)
        return res
