class Solution:
    # 73.14% 37.65%
    def maxSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        res = sum(grid[0][:3]) + sum(grid[2][:3]) + grid[1][1]
        if n == 3:
            for j in range(1, m-2):
                cur_row = sum(grid[0][j:j+3]) + sum(grid[2][j:j+3]) + grid[1][j+1]
                res = max(res, cur_row)
        if m == 3:
            for i in range(1, n-2):
                cur_row = sum(grid[i][:3]) + sum(grid[i+2][:3]) + grid[i+1][1]
                res = max(res, cur_row)
        for i in range(n-2):
            for j in range(m-2):
                cur_row = sum(grid[i][j:j+3]) + sum(grid[i+2][j:j+3]) + grid[i+1][j+1]
                res = max(res, cur_row)
        return res

    # 43.57% 17.06% (55.66% 72.38%)
    def maxSum_v2(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        res = sum(grid[0][:3]) + sum(grid[2][:3]) + grid[1][1]
        for i in range(n-2):
            for j in range(m-2):
                cur_row = sum(grid[i][j:j+3]) + sum(grid[i+2][j:j+3]) + grid[i+1][j+1]
                res = max(res, cur_row)
        return res

    # 52.39% 95.06%
    def maxSum_v3(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        res = 0
        for i in range(n-2):
            for j in range(m-2):
                cur_row = (
                    sum(grid[i][j:j+3]) +
                    sum(grid[i+2][j:j+3]) +
                    grid[i+1][j+1]
                )
                res = max(res, cur_row)
        return res
