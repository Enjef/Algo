class Solution:
    def longestPalindrome(self, s: str) -> str:  # 13.90% 60.84%
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

    def longestPalindrome_mock(self, s: str) -> str:  # 11.87% 60.57%
        if s == s[::-1]:
            return s
        n = len(s)
        size = n-1
        while size > 1:
            for i in range(n-size+1):
                if s[i:i+size] == s[i+size-1:i-n-1:-1]:
                    return s[i:i+size]
            size -= 1
        return s[0]
