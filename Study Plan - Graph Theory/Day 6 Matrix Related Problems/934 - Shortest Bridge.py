class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:  # 5.54% 73.50%
        def bfs(arr):
            while arr:
                temp = set()
                while arr:
                    row, col = arr.pop()
                    grid[row][col] = 0
                    first.add((row, col))
                    for idx in range(4):
                        r, c = row+r_dir[idx], col+c_dir[idx]
                        if -1<r<n and -1<c<n and grid[r][c]==1:
                            temp.add((r, c))
                arr = temp
            return
        
        def find_first():
            for i in range(n):
                for j in range(n):
                    if grid[i][j]:
                        return (i, j)
        
        n = len(grid)
        r_dir = [-1, 1, 0, 0]
        c_dir = [0, 0, -1, 1]
        cur = -1
        first = set()
        bfs([find_first()])
        while first:
            temp = set()
            while first:
                row, col = first.pop()
                if grid[row][col]:
                    return cur
                for idx in range(4):
                    r, c = row+r_dir[idx], col+c_dir[idx]
                    if -1<r<n and -1<c<n:
                        temp.add((r, c))
            first = temp
            cur += 1
        return cur


class Solution_best_speed:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            grid[x][y] = 2
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] == 1: dfs(nx, ny)
                    elif grid[nx][ny] == 0: 
                        q.add((nx, ny))
        m, n = len(grid), len(grid[0])
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = set()
        
        for i, j in product(range(m), range(n)):
            if grid[i][j] == 1:
                dfs(i, j)
                break
        step = 0
        q = deque(q)
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in d:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != 2:
                        if grid[nx][ny] == 1: return step + 1
                        if grid[nx][ny] == 0: grid[nx][ny] = 2
                        q.append((nx, ny))
            step += 1
        return step


class Solution_best_memory:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def isvalid(x, y):
            if x < 0 or x >= m:
                return False
            if y < 0 or y >= n:
                return False
            if grid[x][y] == 2:
                return False
            return True
        
        def bfs1(initx, inity):
            queue = deque([[initx, inity]])
            grid[initx][inity] = 2
            res = deque([])
            while queue:
                posx, posy = queue.popleft()
                res.append([posx, posy])
                for i, j in directions:
                    x, y = posx + i, posy + j
                    if isvalid(x, y):
                        if grid[x][y] == 1:
                            queue.append([x, y])
                            grid[x][y] = 2
            return res
        
        m, n = len(grid), len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        group2 = deque([])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    group2 = bfs1(i, j)
                    break
            if group2:
                break
        step = 0
        while group2:
            length = len(group2)
            step += 1
            for _ in range(length):
                posx, posy = group2.popleft()
                for i, j in directions:
                    x, y = posx + i, posy + j
                    if isvalid(x, y):
                        if grid[x][y] == 1:
                            return step - 1
                        group2.append([x, y])
                        grid[x][y] = 2
                
