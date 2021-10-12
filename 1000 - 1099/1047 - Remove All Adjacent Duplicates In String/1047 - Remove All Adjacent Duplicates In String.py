from string import ascii_lowercase


class Solution:
    def removeDuplicates(self, s: str) -> str:  # slow 5% 7468 ms 34.2 MB
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

    def removeDuplicates_best(self, s: str) -> str:
        duplicates = [2*ch for ch in ascii_lowercase]
        prev_length = -1
        while prev_length != len(s):
            prev_length = len(s)
            for d in duplicates:
                s = s.replace(d, '')
        return s
