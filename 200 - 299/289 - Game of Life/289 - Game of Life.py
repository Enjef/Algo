class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:  # 94.90% 51.25%
        """
        Do not return anything, modify board in-place instead.
        """
        def measure(row, col):
            count = 0
            for y, x in directions:
                yy, xx = row+y, col+x
                if not(-1 < yy < m and -1 < xx < n) or not board[yy][xx]:
                    continue
                count += 1
            if not board[row][col] and count == 3:
                return 1
            elif board[row][col] and count == 2 or count == 3:
                return 1
            else:
                return 0

        out = []
        m, n = len(board), len(board[0])
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for i in range(m):
            new_row = []
            for j in range(n):
                new_row.append(measure(i, j))
            out.append(new_row)
        for i in range(m):
            board[i] = out[i]
        return


class Solution_best_memory:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R, C = len(board), len(board[0])

        def count_neighbors(r, c):
            count = 0
            for i in range(r-1, r+2):
                for j in range(c-1, c+2):
                    if i < 0 or j < 0 or i == R or j == C or (i == r and j == c):
                        continue
                    if board[i][j] in [1, 3]:
                        count += 1
            return count
        for r in range(R):
            for c in range(C):
                nei = count_neighbors(r, c)
                if board[r][c] == 1:
                    if nei in [2, 3]:
                        board[r][c] = 3
                elif nei == 3:
                    board[r][c] = 2

        for r in range(R):
            for c in range(C):
                if board[r][c] in [2, 3]:
                    board[r][c] = 1
                elif board[r][c] == 1:
                    board[r][c] = 0
