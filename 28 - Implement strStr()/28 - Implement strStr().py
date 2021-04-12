class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        try:
            check = haystack.index(needle)
            return check
        except:
            return -1

    def strStr__two(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1





x = Solution()
print(x.strStr__two('a', 'a'))
