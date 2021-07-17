class Solution:
    def largestAltitude(self, gain: List[int]) -> int:  # 98.70% 38.33%
        alt_max = 0
        cur = 0
        for i in range(len(gain)):
            cur += gain[i]
            alt_max = max(alt_max, cur)
        return alt_max
