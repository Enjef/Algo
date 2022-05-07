class Solution:
    def numSub(self, s: str) -> int:  # 82.61% 65.49%
        total = 0
        cur = 0
        for char in s:
            if char == '1':
                cur += 1
            else:
                cur = 0
            total += cur
        return total % (10**9+7)

    def numSub_best_speed(self, s: str) -> int:
        res = 0
        for s_ in s.split('0'):
            l = len(s_)
            res += (1 + l) * l // 2 
        return res % (10 ** 9 + 7)

    def numSub_best_memory(self, s: str) -> int:
        ct, ans = 0, 0
        for i in range(len(s)):
            if s[i] == '0':
                ct = 0
            else:
                ct += 1
                ans += ct
        return ans % ((10**9)+7)
