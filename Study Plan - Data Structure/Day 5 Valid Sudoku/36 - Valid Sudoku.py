class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
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
