class Solution:
    def countBinarySubstrings(self, s: str) -> int:  # 9.60% 9.15%
        count = 0
        stack = [s[0]]
        for i in range(1, len(s)):
            if s[i] == stack[-1][0]:
                stack[-1] = ''.join([stack[-1], s[i]])
            else:
                stack.append(s[i])
        for i in range(1, len(stack)):
            count += min(len(stack[i-1]), len(stack[i]))
        return count

    def countBinarySubstrings_best_speed(self, s: str) -> int:
        consecutive_count = list(
            map(len, s.replace('10', '1 0').replace('01', '0 1').split())
        )
        return sum(map(min, zip(consecutive_count, consecutive_count[1:])))

    def countBinarySubstrings_best_memory(self, s: str) -> int:
        res = 0
        prev = 0
        tmp = 1
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                res += min(prev, tmp)
                prev = tmp
                tmp = 1
            else:
                tmp += 1
        res += min(prev, tmp)
        return res
