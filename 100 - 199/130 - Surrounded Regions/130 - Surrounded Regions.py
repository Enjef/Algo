class Solution:
    def solve(self, board: List[List[str]]) -> None:  # 5.02% 23.01%
        """
        Do not return anything, modify board in-place instead.
        """
        def checker(x, y):
            seen.append((x, y))
            for v, h in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                if (
                        0 <= v < len(board) and
                        0 <= h < len(board[0]) and
                        (v, h) not in seen and
                        board[v][h] == 'O'):
                    checker(v, h)
        seen = []
        for i in [0, len(board)-1]:
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    checker(i, j)
        for i in range(1, len(board)-1):
            for j in [0, len(board[0])-1]:
                if board[i][j] == 'O':
                    checker(i, j)
        for i in range(1, len(board)-1):
            for j in range(1, len(board[0])-1):
                if (i, j) not in seen and board[i][j] == 'O':
                    board[i][j] = 'X'
        return board

    def solve_best_speed(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        seen = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(r, c):
            if board[r][c] == 'O' and (r, c) not in seen:
                seen.add((r, c))
                for direction in directions:
                    nei_r, nei_c = r + direction[0], c + direction[1]
                    if 0 <= nei_r < n and 0 <= nei_c < m:
                        dfs(nei_r, nei_c)
        for i in range(0, n):
            dfs(i, 0)
            dfs(i, m-1)
        for i in range(1, m-1):
            dfs(0, i)
            dfs(n-1, i)
        for r in range(n):
            for c in range(m):
                if board[r][c] == "O" and (r, c) not in seen:
                    board[r][c] = "X"

    def solve_memory_best(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        r = len(board)
        c = len(board[0])
        for i in range(r):
            for j in range(c):
                if not (i == 0 or j == 0 or i == r - 1 or j == c - 1):
                    continue
                self.bfs(board, i, j)
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'E':
                    board[i][j] = 'O'

    def bfs(self, board, i, j):
        queue = deque([(i, j)])
        while queue:
            x, y = queue.popleft()
            if board[x][y] != 'O':
                continue
            board[x][y] = 'E'
            if y < len(board[0]) - 1:
                queue.append((x, y + 1))
            if x < len(board) - 1:
                queue.append((x + 1, y))
            if y > 0:
                queue.append((x, y - 1))
            if x > 0:
                queue.append((x - 1, y))
