class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool: # 15.57% 95.28%
        def bfs(i, j, idx, cur):
            seen = set([(i, j)]) | cur
            res = False
            if idx == len(word) - 1:
                return board[i][j] == word[idx]
            for z in range(len(direction_x)):
                x = j+direction_x[z]
                y = i+direction_y[z]
                if (-1 < x < m and -1 < y < n and
                    board[y][x] == word[idx+1] and
                    (y, x) not in seen):
                        res = res or bfs(y, x, idx+1, seen)
            return res
        n, m = len(board), len(board[0])
        direction_x = [0, -1, 1, 0]
        direction_y = [-1, 0, 0, 1]
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if bfs(i, j, 0, set()):
                        return True
        return False

    def exist_best_speed(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        nbrs : Tuple[Tuple[int]] = ((0, 1), (1, 0), (0, -1), (-1, 0))
        l = len(word)
        flat = [c for b in board for c in b]
        for letter in tuple(set(word)):
            if flat.count(letter) < word.count(letter):
                return False
        if (l > 1 and
            sum(c == word[0] for c in flat) >
            sum(c == word[-1] for c in flat)):
                word = word[::-1]
        
        def dfs(i: int, j: int, s: int) -> bool:
            if s == l:
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[s]:
                return False
            board[i][j] = -1
            for dx, dy in nbrs:
                if dfs(i + dx, j + dy, s + 1):
                    return True
            board[i][j] = word[s]
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False



    def exist_best_memory(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()
        def dfs(r, c, i):                
            if i == len(word):
                return True
            if (r < 0 or
                c < 0 or
                r >= rows or
                c >= cols or
                board[r][c] != word[i] or
                (r,c) in path
               ):
                return False
            path.add((r,c))
            res = (
                dfs(r+1, c, i+1) or
                dfs(r-1, c, i+1) or
                dfs(r, c+1, i+1) or
                dfs(r, c-1, i+1)
            )
            path.remove((r,c))
            return res
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
