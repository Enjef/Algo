class Solution:
    def getSmallestString(self, n: int, k: int) -> str:  # 83.44% 72.54%
        i = n - 1
        out = ['a'] * n
        k -= n
        for i in range(n-1, -1, -1):
            if k > 25:
                out[i] = 'z'
                k -= 25
            else:
                out[i] = chr(ord('a')+k)
                break
        return ''.join(out)

    def getSmallestString_2nd_best_speed(self, n: int, k: int) -> str:
        d, m = divmod(k-n, 25)
        return 'a' * (n-1-d) + (chr(m+97) if d != n else '') + 'z' * d


class Solution_best_speed:
    @staticmethod
    def get_char(num: int):
        return chr(97 + num)

    def getSmallestString(self, n: int, k: int) -> str:
        remainder = k - n
        z_chars = 0
        balancer = ''
        if remainder > 25:
            z_chars = remainder // 25
            remainder -= z_chars * 25
        if remainder:
            balancer = Solution.get_char(remainder)
        a_chars = n - len(balancer) - z_chars
        return 'a'*a_chars + balancer + 'z'*z_chars


class Solution_best_memory:
    @staticmethod
    def get_char(num: int):
        return chr(97 + num)

    def getSmallestString(self, n: int, k: int) -> str:
        remainder = k - n
        z_chars = 0
        if remainder > 25:
            z_chars = remainder // 25
            remainder -= z_chars * 25
            if z_chars == n:
                return 'z'*n
        balancer_char = Solution.get_char(remainder)
        a_chars = n - 1 - z_chars
        return 'a'*a_chars + balancer_char + 'z'*z_chars
