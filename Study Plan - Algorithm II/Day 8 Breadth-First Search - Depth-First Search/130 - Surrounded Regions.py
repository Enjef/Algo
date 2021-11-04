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
        return

    def solve_v2(self, board: List[List[str]]) -> None:  # 5.00% 68.42%
        """
        Do not return anything, modify board in-place instead.
        """
        def checker(x, y):
            visited.append((x, y))
            for xx, yy in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if (
                        not(0 < xx < m and 0 < yy < n) or
                        board[xx][yy] == 'X' or (xx, yy) in visited):
                    continue
                checker(xx, yy)
            return
        m = len(board)
        n = len(board[0])
        visited = []
        for i in [0, m-1]:
            for j in range(n):
                if board[i][j] == 'O':
                    checker(i, j)
        for j in [0, n-1]:
            for i in range(1, m-1):
                if board[i][j] == 'O':
                    checker(i, j)
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and board[i][j] == 'O':
                    board[i][j] = 'X'
        return
