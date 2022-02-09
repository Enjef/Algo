class Solution:
    def validPalindrome(self, s: str) -> bool:  # 38.23%  68.74%
        def parts(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        n = len(s)
        i, j = 0, n - 1
        while i < j:
            if s[i] != s[j]:
                return parts(i+1, j) | parts(i, j-1)
            i += 1
            j -= 1
        return True

    def validPalindrome_best_speed(self, s: str) -> bool:
        helper = lambda s: s == s[::-1]
        i, j, x = 0, len(s) - 1, len(s) >> 1
        while i < j:
            if s[i: i + x] == s[j: j - x: -1]:
                i += x
                j -= x
            elif x > 1:
                x >>= 1
            else:
                return helper(s[i: j]) or helper(s[i + 1: j + 1])
        return True

    def validPalindrome_best_memory(self, s: str) -> bool:
        def check(s):
            return s == s[::-1]
        if check(s): 
            return True 
        i,j = 0,len(s)-1
        while i<j:
            if s[i] != s[j]:
                return check(s[:i]+s[i+1:]) or check(s[:j]+s[j+1:])
            i+=1
            j-=1
