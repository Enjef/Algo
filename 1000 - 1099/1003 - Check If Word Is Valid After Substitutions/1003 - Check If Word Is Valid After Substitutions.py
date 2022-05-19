class Solution:
    def isValid(self, s: str) -> bool:  # 69.85% 89.25%
        while 'abc' in s:
            s = s.replace('abc', '')
        return s == ''

    def isValid_v2(self, s: str) -> bool:  # 45.97% 22.99%
        stack = []
        for char in s:
            if char == 'c' and stack[-2:] == ['a', 'b']:
                stack.pop()
                stack.pop()
            else:
                stack.append(char)
        return not stack

    def isValid_best_speed(self, s: str) -> bool:
        n = len(s)
        count = 0
        while len(s) > 0:
            if 'abc' in s:
                s = s.replace('abc', '')
                count += 1
            else:
                break
        if len(s) > 0:
            return False
        else:
            return True

    def isValid_2nd_best_speed(self, s: str) -> bool:
        while 'abc' in s:
            s = s.replace('abc', '')
        return s == ''
