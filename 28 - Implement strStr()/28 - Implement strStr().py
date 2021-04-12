class Solution:

    # 1
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        try:
            return haystack.index(needle)
        except:
            return -1

    # 3
    def strStr_index(self, haystack, needle):
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)

    # 2
    def strStr__two(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        for i in range(len(haystack)-len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


x = Solution()
print(x.strStr_index('a', 'a'))
