class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:  # (ok)slow 21.65%
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

    def maxAreaOfIsland_stack(
            self,
            grid: List[List[int]]) -> int:  # 14.34% 80.16%
        size_max = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j]:
                    continue
                stack = [(i, j)]
                size = 0
                while stack:
                    x, y = stack.pop()
                    if (
                            0 <= x < len(grid) and
                            0 <= y < len(grid[0]) and
                            grid[x][y] == 1):
                        grid[x][y] = 0
                        size += 1
                        stack.extend([(x+1, y), (x-1, y), (x, y+1), (x, y-1)])
                size_max = max(size_max, size)
        return size_max
