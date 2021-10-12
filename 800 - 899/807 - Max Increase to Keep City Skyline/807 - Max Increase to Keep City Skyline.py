class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        up = [-1]*len(grid)
        left = [-1]*len(grid)
        count = 0
        for i in range(len(grid)):
            left[i] = max(grid[i])
            for j in range(len(grid)):
                up[j] = max(up[j], grid[i][j])
        for i in range(len(grid)):
            for j in range(len(grid)):
                count += abs(min(up[j], left[i]) - grid[i][j])
        return count
