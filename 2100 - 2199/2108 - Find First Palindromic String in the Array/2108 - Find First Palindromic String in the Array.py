class Solution:
    def firstPalindrome(self, words: List[str]) -> str:  # 8.85(22.21)% 99.02%
        for word in words:
            if word == word[::-1]:
                return word
        return ''

    def firstPalindrome_v2(self, words: List[str]) -> str:  # 6.46% 96.65%
        for word in words:
            i, j = 0, len(word)-1
            while i < j:
                if word[i] != word[j]:
                    break
                i += 1
                j -= 1
            if i >= j:
                return word
        return ''

    def firstPalindrome_v3(self, words: List[str]) -> str:  # 18.06% 96.65%
        for word in words:
            i, n = 0, len(word)
            for i in range(n):
                if word[i] != word[n-1-i]:
                    break
            if i >= n // 2:
                return word
        return ''

    def firstPalindrome_best_speed(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ''
