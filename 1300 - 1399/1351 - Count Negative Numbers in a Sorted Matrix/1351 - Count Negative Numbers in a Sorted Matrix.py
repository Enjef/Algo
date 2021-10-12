class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:  # 81.21%  47.11%
        out = 0
        for row in grid:
            for i in range(len(row)):
                if row[i] < 0:
                    out += len(row[i:])
                    break
        return out

    def countNegatives_best(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        cnt = 0
        row = n-1
        col = 0
        while(row >= 0 and col < m):
            if grid[row][col] < 0:
                cnt += m - col
                row -= 1
                col = 0
            else:
                col += 1
        return cnt

    def countNegatives_short(self, grid: List[List[int]]) -> int:
        return sum(x < 0 for row in grid for x in row)
