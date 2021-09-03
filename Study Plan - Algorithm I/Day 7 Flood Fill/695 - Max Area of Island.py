class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        out = 0
        visited = []
        n, m = len(grid), len(grid[0])

        def helper(row, col):
            if [row, col] in visited or grid[row][col] != 1:
                return 0
            visited.append([row, col])
            count = 0
            if col > 0:
                count += helper(row, col - 1)
            if col + 1 < m:
                count += helper(row, col + 1)
            if row > 0:
                count += helper(row - 1, col)
            if row + 1 < n:
                count += helper(row + 1, col)
            return count + 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                score = helper(i, j)
                out = max(out, score)
        return out
