class Solution:
    def minAddToMakeValid(self, s: str) -> int: # 32.33% 88.75%
        stack = []
        out = 0
        for char in s:
            if char == ')':
                if not stack:
                    out += 1
                else:
                    stack.pop()
            elif char == '(':
                stack.append('(')
        out += len(stack)
        return out

    def minAddToMakeValid_best_speed(self, s: str) -> int:
        open_count = 0
        close_count = 0
        for char in s:
            if char == '(':
                open_count +=1
            if char == ')':
                if open_count > 0:
                    open_count -=1
                else:
                    close_count +=1
        return open_count + close_count

    def minAddToMakeValid_2nd_best_speed(self, s: str) -> int:
        balance = 0
        ans = 0
        for c in s:
            balance += 1 if c == '(' else -1
            if balance == -1:
                ans += 1
                balance += 1
        return ans + balance
