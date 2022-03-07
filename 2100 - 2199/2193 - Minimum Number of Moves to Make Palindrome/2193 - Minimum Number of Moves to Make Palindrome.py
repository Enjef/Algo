class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:  # 100.00% 42.86%
        res = 0
        s = list(s)
        while s:
            idx = s.index(s[-1])
            if idx == len(s)-1:
                res += idx // 2
            else:
                res += idx
                s.pop(idx)
            s.pop()
        return res

    def minSwapsToBePalindrome_best_speed_and_memory(self, s: str) -> int:
        s = list(s)
        f, b = 0, len(s) - 1
        swaps = 0
        while f < b:
            mid = b
            while f < mid and s[f] != s[mid]:
                mid -= 1
            if f == mid:
                s[f], s[f + 1] = s[f + 1], s[f]
                swaps += 1
                continue
            for i in range(mid, b):
                s[i], s[i + 1] = s[i + 1], s[i]
                swaps += 1
                i += 1
            f += 1
            b -= 1
        return swaps
