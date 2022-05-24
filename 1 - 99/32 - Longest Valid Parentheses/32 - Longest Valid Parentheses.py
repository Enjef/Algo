class Solution:
    def longestValidParentheses(self, s: str) -> int:  # 15.64% 99.13%
        result = 0
        left = right = 0
        n = len(s)
        for i in range(n):
            if s[i] == ')':
                right += 1
            else:
                left += 1
            if left == right:
                result = max(result, left*2)
            if left < right:
                left = right = 0
        left = right = 0
        for i in range(n-1,-1,-1):
            if s[i] == ')':
                right += 1
            else:
                left += 1
            if left == right:
                result = max(result, left*2)
            if left > right:
                left = right = 0
        return result

    def longestValidParentheses_best_speed(self, s: str) -> int:
        stack = [-1]
        res = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    res = max(res, i - stack[-1])
                else:
                    stack.append(i)
        return res



