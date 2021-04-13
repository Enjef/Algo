class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        out = 0
        if len(s) == 1 and s[0] == ' ':
            return 0
        if len(s) == 1 and s[0] != ' ':
            return 1
        for char in range(len(s)-1, -1, -1):
            if out and s[char] == ' ':
                break
            if s[char] != ' ':
                out += 1
        if out:
            return out
        return 0


x = Solution()
print(x.lengthOfLastWord('a '))
