class Solution:
    def hammingWeight(self, n: int) -> int:  # 71.24% 5.64%
        return str(bin(n)).count('1')
