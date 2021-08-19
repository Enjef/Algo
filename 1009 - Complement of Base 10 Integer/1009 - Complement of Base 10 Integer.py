class Solution:
    def bitwiseComplement(self, n: int) -> int:  # 83.33% 7.08%
        return int(
            ''.join(['0' if x == '1' else '1' for x in str(bin(n))[2:]]), 2
        )

    def bitwiseComplement_best_speed(self, n: int) -> int:
        if n == 0:
            return 1
        x = 1
        while x < n:
            x = x*2 + 1
        return x ^ n

    def bitwiseComplement_memory(self, n: int) -> int:
        bin_num = list(bin(n))
        for i in range(2, len(bin_num)):
            if bin_num[i] == '1':
                bin_num[i] = '0'
            else:
                bin_num[i] = '1'
        ans = "".join(bin_num)
        return int(ans, 2)
