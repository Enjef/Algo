class Solution:
    def numSteps(self, s: str) -> int:  # 30.48% 22.30%
        num = int(s, 2)
        result = 0
        while num != 1:
            if num % 2:
                num += 1
            else:
                num //= 2
            result += 1
        return result

    def numSteps_best_speed(self, s: str) -> int:
        res = 0
        num = int(s, 2)
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num + 1
            res += 1
        return res

    def numSteps_2nd_best_speed(self, s: str) -> int:
        res = 0
        while s != '1':
            n = len(s)
            if s[-1] == '1':
                i = n - 1
                while i >= 0:
                    if s[i] == '0':
                        break
                    i -= 1
                if i == -1:
                    s = '1' + '0' * n
                else:
                    s = s[:i] + '1' + '0' * (n - 1 - i)
            else:
                s = s[: -1]
            res += 1
        return res

    def numSteps_best_memory(self, s: str) -> int:
        ans = 0
        carry = 0
        n = len(s)
        for i in range(n-1, 0, -1):
            if int(s[i]) + carry == 1:
                carry = 1
                ans += 2
            else:
                ans += 1
        return ans + carry
