class Solution:
    def strStr(self, haystack: str, needle: str) -> int:  # 98.17% 42.88%
        try:
            return haystack.index(needle)
        except:
            return -1
