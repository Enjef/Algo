class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:  # 5.13% 21.52%
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

    def maxAreaOfIsland_best_speed(self, grid: List[List[int]]) -> int:
        m = len(grid) - 1
        n = len(grid[0]) - 1

        def dfs(i: int, j: int):
            grid[i][j] = 0
            area = 1
            if i > 0 and grid[i - 1][j]:
                area += dfs(i - 1, j)
            if j < n and grid[i][j + 1]:
                area += dfs(i, j + 1)
            if i < m and grid[i + 1][j]:
                area += dfs(i + 1, j)
            if j > 0 and grid[i][j - 1]:
                area += dfs(i, j - 1)
            return area
        return max(
            (
                dfs(i, j) for i in range(m + 1) for j in range(n + 1) if
                grid[i][j]), default=0
            )

    def maxAreaOfIsland_best_memory(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_area = 0
        for ii in range(m):
            for jj in range(n):
                if grid[ii][jj] == 1:
                    grid[ii][jj] = 0
                    queue, temp_area = [[ii, jj]], 1
                    while len(queue) > 0:
                        row, col = queue[0][0], queue[0][1]
                        if row-1 >= 0:
                            if grid[row-1][col] == 1:
                                grid[row-1][col] = 0
                                queue.append([row-1, col])
                                temp_area += 1
                        if row+1 <= m-1:
                            if grid[row+1][col] == 1:
                                grid[row+1][col] = 0
                                queue.append([row+1, col])
                                temp_area += 1
                        if col-1 >= 0:
                            if grid[row][col-1] == 1:
                                grid[row][col-1] = 0
                                queue.append([row, col-1])
                                temp_area += 1
                        if col+1 <= n-1:
                            if grid[row][col+1] == 1:
                                grid[row][col+1] = 0
                                queue.append([row, col+1])
                                temp_area += 1
                        queue.pop(0)
                    if temp_area > max_area:
                        max_area = temp_area
        return(max_area)
