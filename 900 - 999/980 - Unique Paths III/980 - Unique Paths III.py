class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int: # 12.78% 5.70%
        n, m = len(grid), len(grid[0])
        all_sqares = 0
        out = 0
        dir_y = [-1, 0, 0, 1]
        dir_x = [0, -1, 1, 0]
        start_y, start_x = None, None
        for i in range(n):
            for j in range(m):
                if not grid[i][j]:
                    all_sqares += 1
                if grid[i][j] == 1:
                    start_y, start_x = i, j
        stack = []
        for idx in range(4):
            stack.append((start_y+dir_y[idx], start_x+dir_x[idx], 0, set()))
        while stack:
            temp = []
            while stack:
                y, x, way_len, way = stack.pop()
                if not (
                    -1 < y < n and -1 < x < m and
                    grid[y][x] not in {1, -1} and (y, x) not in way):
                        continue
                if grid[y][x] == 2:
                    if way_len == all_sqares:
                        out += 1
                        continue
                    continue
                way.add((y, x))
                way_len += 1
                for pos in range(4):
                    yy, xx = y + dir_y[pos], x + dir_x[pos]
                    temp.append((yy, xx, way_len, way.copy()))
            stack = temp
        return out

class Solution_best_speed:
    def __init__(self):
        self.ans = 0
        
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        tot = n * m
        tot -= 2
        
        def panda(i, j, cnt, vis):
            vis[i][j] = True
            if grid[i][j] == 0:
                cnt += 1
            if grid[i][j] == 2:
                if cnt == tot:
                    self.ans += 1
                vis[i][j] = False
                return self.ans
            if i + 1 < n and grid[i + 1][j] != -1 and not vis[i + 1][j]:
                panda(i + 1, j, cnt, vis)
            if j + 1 < m and grid[i][j + 1] != -1 and not vis[i][j + 1]:
                panda(i, j + 1, cnt, vis)
            if i - 1 >= 0 and grid[i - 1][j] != -1 and not vis[i - 1][j]:
                panda(i - 1, j, cnt, vis)
            if j - 1 >= 0 and grid[i][j - 1] != -1 and not vis[i][j - 1]:
                panda(i, j - 1, cnt, vis)
            vis[i][j] = False
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    sti = i
                    stj = j
                elif grid[i][j] == -1:
                    tot -= 1
        vis = [[False for i in range(m)] for j in range(n)]
        panda(sti, stj, 0, vis)
        return self.ans

class Solution_2nd_best_speed:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        last_row = len(grid)-1
        last_col = len(grid[0])-1
        start = []
        end = []
        
        steps = 0
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == 1:
                    start = (i, j)
                elif col == 2:
                    end = (i, j)
                elif col == 0:
                    steps += 1
        
        def take_step(g: List[List[int]], i, j, step_count) -> int:
            found_paths = 0
            g[i][j] = 1
            if i > 0:
                if g[i-1][j] == 2 and step_count == steps:
                    found_paths += 1
                elif g[i-1][j] == 0:
                    found_paths += take_step(g, i-1, j, step_count+1)
            if j > 0:
                if g[i][j-1] == 2 and step_count == steps:
                    found_paths += 1
                elif g[i][j-1] == 0:
                    found_paths += take_step(g, i, j-1, step_count+1)
            if i < last_row:
                if g[i+1][j] == 2 and step_count == steps:
                    found_paths += 1
                elif g[i+1][j] == 0:
                    found_paths += take_step(g, i+1, j, step_count+1)
            if j < last_col:
                if g[i][j+1] == 2 and step_count == steps:
                    found_paths += 1
                elif g[i][j+1] == 0:
                    found_paths += take_step(g, i, j+1, step_count+1)
            g[i][j] = 0
            return found_paths
        return take_step(grid, start[0], start[1], 0)
        
class Solution_best_memory:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        result = 0
        empty_squares = sum(1 for row in grid for cell in row if cell == 0)
        def explore(i, j, count):
            nonlocal result, empty_squares
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] in [-1, -2]:
                return
            if grid[i][j] == 2:
                if count == empty_squares:
                    result += 1
            else:
                val = grid[i][j]
                if val == 0:
                    count += 1
                grid[i][j] = -2
                explore(i-1, j, count)
                explore(i+1, j, count)
                explore(i, j-1, count)
                explore(i, j+1, count)
                grid[i][j] = val
        i,j = next((i,j) for i,row in enumerate(grid) for j,cell in enumerate(row) if cell == 1)
        explore(i, j, 0)
        return result
