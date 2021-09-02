class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:  # 69.44% 42.84%
        check = []
        for block_row in range(0, 7, 3):
            for block in range(0, 7, 3):
                for row in range(3):
                    check += board[row + block_row][block:block+3]
                check = [x for x in check if x != '.']
                if len(check) != len(set(check)):
                    return False
                check = []
        for i in range(9):
            check = [x for x in board[i] if x != '.']
            if len(check) != len(set(check)):
                return False
            check = [row[i] for row in board if row[i] != '.']
            if len(check) != len(set(check)):
                return False
        return True

    def isValidSudoku_lp_day_5(
            self,
            board: List[List[str]]) -> bool:  # 6.17% 70.08%
        for row in range(0, 7, 3):
            for block in range(0, 7, 3):
                square = []
                for i in range(3):
                    square.extend(
                        [x for x in board[i+row][block:block+3] if x.isdigit()]
                    )
                if len(set(square)) != len(square):
                    return False
        cols = [x for x in zip(*board)]
        for i in range(len(board)):
            col = [x for x in cols[i] if x.isdigit()]
            row = [x for x in board[i] if x.isdigit()]
            if len(col) != len(set(col)) or len(row) != len(set(row)):
                return False
        return True

    def isValidSudoku_speed_best(self, board: List[List[str]]) -> bool:
        row = [set() for _ in board]
        column = [set() for _ in board]
        square = [set() for _ in board]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                if board[i][j] in row[i]:
                    return False
                row[i].add(board[i][j])
                if board[i][j] in column[j]:
                    return False
                column[j].add(board[i][j])
                curr_row = i // 3
                curr = curr_row * 3 + j//3
                if board[i][j] in square[curr]:
                    return False
                square[curr].add(board[i][j])
        return True
