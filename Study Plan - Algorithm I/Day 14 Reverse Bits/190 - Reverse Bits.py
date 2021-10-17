class Solution:
    def reverseBits(self, n: int) -> int:  # 77.76% 6.53%
        s = list(bin(n)[2:].zfill(32))
        return int(''.join(s)[::-1], 2)
