class Solution:
    def longestPalindrome(self, s: str) -> str:
        p_max = s[0]
        if s == s[::-1]:
            return s
        size = 2
        while size <= len(s):
            for i in range(len(s)-size + 1):
                current = s[i:i+size]
                if current != current[::-1]:
                    continue
                p_max = current
            size += 1
        return p_max


x = Solution()
x.longestPalindrome('abb')
