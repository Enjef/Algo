class Solution:
    def nearestExit(self, maze, entrance):  # 53.38% 95.57%
        m, n = len(maze), len(maze[0])        
        er, ec = entrance
        borders = set()
        r_dir = [-1, 1, 0, 0]
        c_dir = [0, 0, -1, 1]
        for i in range(m):
            if maze[i][0] == '.':
                borders.add((i, 0))
            if maze[i][n-1] == '.':
                borders.add((i, n-1))
        for i in range(n):
            if maze[0][i] == '.':
                borders.add((0, i))
            if maze[m-1][i] == '.':
                borders.add((m-1, i))
        borders.discard((er, ec))
        res = 0
        while borders:
            temp = set()
            while borders:
                r, c = borders.pop()
                if (r, c) == (er, ec):
                    return res
                maze[r][c] = '+'
                for i in range(4):
                    row, col = r+r_dir[i], c+c_dir[i]
                    if -1<row<m and -1<col<n and maze[row][col] == '.':
                        temp.add((row, col))
            borders = temp
            res += 1
        return -1


class Solution_best_speed:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n  = len(maze[0])
        queue = deque()
        queue.append(entrance)
        level = 0
        while len(queue) > 0:
            levelSize = len(queue)
            while levelSize > 0:
                i, j = queue.popleft()
                if i != entrance[0] or j != entrance[1]:
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        return level
                if i > 0 and maze[i - 1][j] == '.':
                    maze[i - 1][j] = '1'
                    queue.append([i - 1, j])
                if i < m - 1 and maze[i + 1][j] == '.':
                    maze[i + 1][j] = '1'
                    queue.append([i + 1, j])
                if j > 0 and maze[i][j - 1] == '.':
                    maze[i][j - 1] = '1'
                    queue.append([i, j - 1])
                if j < n - 1 and maze[i][j + 1] == '.':
                    maze[i][j + 1] = '1'
                    queue.append([i, j + 1])
                levelSize -= 1
            level += 1
        return -1


class Solution_best_memory:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def isexit(r, c):
            return [r, c] != entrance and (r == 0 or c == 0 or r == len(maze)-1 or c == len(maze[0])-1)
        
        def isvalid(r, c):
            return  0 <= r < len(maze) and 0 <= c < len(maze[0])

        q = deque([(entrance, 0)])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while q:
            cell, steps = q.popleft()
            r, c = cell
            if isexit(r, c):
                return steps
            for dx, dy in directions:
                nr, nc = r +dx, c+dy
                if isvalid(nr, nc) and maze[nr][nc] != "+":
                    q.append(([nr, nc], steps+1))
                    maze[nr][nc] = "+"
        return -1
