class Solution:
    def trap(self, height: List[int]) -> int:  # 68.39% 86.21%
        n = len(height)
        dp = [0]*n
        dp[0] = height[0]
        ans = 0
        for i in range(1, n):
            dp[i] = max(height[i], dp[i-1])
        dp[-1] = height[-1]
        for i in range(n-2, -2, -1):
            level = min(dp[i], dp[i+1])
            if height[i] < level:
                ans += level-height[i]
            dp[i] = max(dp[i+1], height[i])
        return ans
