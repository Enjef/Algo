class Solution:
    def maxArea(self, height) -> int:
        v_max = float('-inf')
        left = 0
        right = len(height) - 1
        if len(height) == 2:
            return min(height[0], height[1])
        while left < right:
            v_max = max(v_max, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return v_max


x = Solution()
print(x.maxArea([1, 2, 44, 4]))