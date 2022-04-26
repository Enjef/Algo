class Solution:
    def maxSideLength(
            self, mat: List[List[int]], threshold: int) -> int:  # 35.49 28.23%
        m, n = len(mat), len(mat[0])
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + mat[i-1][j-1]

        max_side = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if min(i, j) < max_side:
                    continue
                left = 0
                right = min(i, j)
                while left <= right:
                    mid = (left+right)//2
                    pref_sum = dp[i][j] - dp[i-mid][j] - dp[i][j-mid] + dp[i-mid][j-mid]
                    if pref_sum <= threshold:
                        max_side = max(max_side, mid)
                        left = mid + 1
                    else:
                        right = mid - 1
        return max_side
