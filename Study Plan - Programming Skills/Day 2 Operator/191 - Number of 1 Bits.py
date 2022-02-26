class Solution:
    def hammingWeight(self, n: int) -> int: # 40.92% 78.07%
        return str(bin(n)).count('1')
