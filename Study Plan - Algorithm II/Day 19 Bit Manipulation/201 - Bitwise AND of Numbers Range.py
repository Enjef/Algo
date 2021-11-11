class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:  # 78.30% 25.24%
        p = 0
        while left != right:
            left >>= 1
            right >>= 1
            p += 1
        return left << p
