class Solution:
    # 33.35% 13.13% (23.95% 96.39%)
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ''
        for i in range(n//2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        return palindrome[:-1] + 'b'




    def breakPalindrome_best_memory(self, pal):
        n = len(pal)
        for i in range(n//2):
            if pal[i] != 'a':
                return pal[:i] + 'a' + pal[i+1:]
        return pal[:-1] + 'b' if n > 1 else ''
