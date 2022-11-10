class Solution:
    # TLE in november 2022
    def removeDuplicates(self, s: str) -> str:
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                return self.removeDuplicates(s[:i-1]+s[i+1:])
        return s

    def removeDuplicates_2(self, s: str) -> str:  # 54.51% 80 ms 14.9 MB
        stack = []
        s_list = list(s)  # can be deleted
        for i in range(len(s_list)):
            if stack and stack[-1] == s_list[i]:
                stack.pop()
            else:
                stack.append(s_list[i])
        return ''.join(stack)

    # 49.57% 18.64% (77.11% 18.64%)
    def removeDuplicates_v3(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)


class Solution_best_speed:
    def removeDuplicates(self, s: str) -> str:
        string = s
        stack = []
        for letter in string:
            if stack and stack[-1] == letter:
                stack.pop()
            else:
                stack.append(letter)
        return ''.join(stack)


class Solution_best_memory:
    def removeDuplicates_1st(self, s: str) -> str:
        s = list(s)
        i = 0
        while i < len(s)-1:
            if s[i] == s[i+1]:
                s.pop(i)
                s.pop(i)
                if i > 0:
                    i -= 1
            if i > len(s)-2:
                return ''.join(s)
            if s[i] != s[i+1]:
                i += 1
        return ''.join(s)

    def removeDuplicates_2nd(self, s: str) -> str:
        res = []
        for c in s:
            if len(res) > 0 and res[-1] == c:
                res.pop()
            else:
                res.append(c)
        return ''.join(res)
