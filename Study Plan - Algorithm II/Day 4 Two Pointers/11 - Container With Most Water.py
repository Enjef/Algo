class Solution:
    def maxArea(self, height: List[int]) -> int:  # 30.19% 57.02%
        i, j = 0, len(height) - 1
        v_max = 0
        while i < j:
            v_max = max(v_max, (j - i) * min(height[i],height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return v_max
