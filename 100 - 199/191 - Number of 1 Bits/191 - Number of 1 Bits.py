class Solution:
    def hammingWeight(self, n: int) -> int:  # 68.68% 5.53%
        return str(bin(n)).count('1')

    def hammingWeight_mock(self, n: int) -> int:  # 96.91% 89.17%
        return str(bin(int(n))).count('1')
