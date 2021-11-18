class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:  # 12.09% 70.78%
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

    def isValidSudoku_v2(self, board: List[List[str]]) -> bool: # 75.44% 70.78%
        for i in range(9):
            row = [x for x in board[i] if x.isdigit()]
            if len(set(row)) != len(row):
                return False
        for col in zip(*board):
            col = [x for x in col if x.isdigit()]
            if len(set(col)) != len(col):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                block = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
                block = [x for x in block if x.isdigit()]
                if len(set(block)) != len(block):
                    return False
        return True
