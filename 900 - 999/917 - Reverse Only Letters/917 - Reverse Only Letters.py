class Solution:
    def reverseOnlyLetters(self, s: str) -> str:  # 5.53% 98.89%
        not_alph = {}
        clean = []
        for i in range(len(s)):
            if not s[i].isalpha():
                not_alph[i] = s[i]
            else:
                clean.append(s[i])
        clean.reverse()
        for i in not_alph:
            clean.insert(i, not_alph[i])
        return ''.join(clean)

    def reverseOnlyLetters_best_speed(self, s: str) -> str:
        l, r = 0, len(s)-1
        res = list(s)
        while l < r:
            if not res[l].isalpha():
                l += 1
            elif not res[r].isalpha():
                r -= 1
            else:
                res[l], res[r] = res[r], res[l]
                l += 1
                r -= 1
        return ''.join(res)
