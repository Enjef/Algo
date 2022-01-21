class Solution:
    def tictactoe_bingo(self, moves: List[List[int]]) -> str:  # 13.78% 69.57%
        winner = {
            True: 'A',
            False: 'B'
        }
        first_row = set([(0, 0), (0, 1), (0, 2)])
        second_row = set([(1, 0), (1, 1), (1, 2)])
        third_row = set([(2, 0), (2, 1), (2, 2)])
        first_col = set([(0, 0), (1, 0), (2, 0)])
        second_col = set([(0, 1), (1, 1), (2, 1)])
        third_col = set([(0, 2), (1, 2), (2, 2)])
        dia = set([(0, 0), (1, 1), (2, 2)])
        second_dia = set([(0, 2), (1, 1), (2, 0)])
        total = set(
            [(0, 0), (0, 1), (0, 2),
             (1, 0), (1, 1), (1, 2),
             (2, 0), (2, 1), (2, 2)]
        )
        win_one = [first_row, second_row, third_row,
                   first_col, second_col, third_col,
                   dia, second_dia
                   ]
        import copy
        win_two = copy.deepcopy(win_one)
        turn = True
        for coord in moves:
            if turn:
                win = win_one
            else:
                win = win_two
            for condition in win:
                condition.discard(tuple(coord))
                total.discard(tuple(coord))
                if not condition:
                    return winner[turn]
            if not total:
                return 'Draw'
            turn = not turn
        return 'Pending'

    def tictactoe_v2(self, moves: List[List[int]]) -> str:  # 18.37% 39.74%
        grid = []
        n = 1
        for _ in range(3):
            row = []
            for _ in range(3):
                row.append(n)
                n += 1
            grid.append(row)
        first = True
        for x, y in moves:
            if first:
                grid[x][y] = 'X'
            else:
                grid[x][y] = 'O'
            first = not first
        if grid[0][0] == grid[0][1] == grid[0][2]:
            return 'A' if grid[0][0] == 'X' else 'B'
        if grid[1][0] == grid[1][1] == grid[1][2]:
            return 'A' if grid[1][0] == 'X' else 'B'
        if grid[2][0] == grid[2][1] == grid[2][2]:
            return 'A' if grid[2][0] == 'X' else 'B'
        if grid[0][0] == grid[1][0] == grid[2][0]:
            return 'A' if grid[0][0] == 'X' else 'B'
        if grid[0][1] == grid[1][1] == grid[2][1]:
            return 'A' if grid[0][1] == 'X' else 'B'
        if grid[0][2] == grid[1][2] == grid[2][2]:
            return 'A' if grid[0][2] == 'X' else 'B'
        if (
                grid[0][0] == grid[1][1] == grid[2][2] or
                grid[0][2] == grid[1][1] == grid[2][0]):
            return 'A' if grid[1][1] == 'X' else 'B'
        if len(moves) == 9:
            return 'Draw'
        return 'Pending'

    def tictactoe_best_speed(self, moves: List[List[int]]) -> str:
        matrix = [[-1] * 3 for i in range(3)]
        player = {0: 'A', 1: 'B'}
        for i, move in enumerate(moves):
            matrix[move[0]][move[1]] = i % 2
        for x in range(3):
            if (
                    matrix[x][0] == matrix[x][1] == matrix[x][2] and
                    matrix[x][0] != -1):
                return player[matrix[x][0]]
            if (
                    matrix[0][x] == matrix[1][x] == matrix[2][x] and
                    matrix[0][x] != -1):
                return player[matrix[0][x]]
        if matrix[0][0] == matrix[1][1] == matrix[2][2] and matrix[0][0] != -1:
            return player[matrix[0][0]]
        if matrix[0][2] == matrix[1][1] == matrix[2][0] and matrix[0][2] != -1:
            return player[matrix[0][2]]
        if len(moves) < 9:
            return 'Pending'
        return 'Draw'

    def tictactoe_best_memory(self, moves: List[List[int]]) -> str:
        n = 3
        hori = [0]*n
        vert = [0]*n
        diag = anti_diag = 0
        player = 1
        for x, y in moves:
            hori[x] += player
            vert[y] += player
            if x == y:
                diag += player
            if x+y == n-1:
                anti_diag += player
            if abs(hori[x]) == n:
                return 'A' if player == 1 else 'B'
            if abs(vert[y]) == n:
                return 'A' if player == 1 else 'B'
            if abs(diag) == 3 or abs(anti_diag) == 3:
                return 'A' if player == 1 else 'B'
            player *= -1
        return 'Draw' if len(moves) == n*n else 'Pending'
