class Solution:
    def isValid(self, s: str) -> bool:
        p_map = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
                continue
            if char in p_map and stack[-1] == p_map[char]:
                stack.pop()
            else:
                stack.append(char)
        return False if stack else True
