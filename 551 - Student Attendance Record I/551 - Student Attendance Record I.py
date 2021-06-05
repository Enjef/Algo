class Solution:
    def checkRecord(self, s: str) -> bool:  # 6% 11%
        return s.count('A') < 2 and 'LLL' not in s
