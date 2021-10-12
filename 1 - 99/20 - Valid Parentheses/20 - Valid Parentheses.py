dict_a = {
    '(': ')',
    '[': ']',
    '{': '}',
}


class Solution:
    def isValid(self, s: str) -> bool:  # 66.02%  64.36%
        if len(s) == 1:
            return False
        if s[0] not in dict_a:
            return False
        temp = ''
        for i in range(len(s)):
            if s[i] in dict_a:
                temp += s[i]
                continue
            if s[i] not in dict_a:
                if not temp or s[i] != dict_a[temp[-1]]:
                    return False
                if temp and s[i] == dict_a[temp[-1]]:
                    temp = temp[:-1]
                    continue
        return temp == ''

    def isValid_sp_day_9(self, s: str) -> bool:  # 96.05% 86.99%
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
