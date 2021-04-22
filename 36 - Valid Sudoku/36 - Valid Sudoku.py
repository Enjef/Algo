board = [
    [".", ".", ".", ".", "5", ".", ".", "1", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "1"],

    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],

    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."]
]


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
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


x = Solution()
print(x.isValidSudoku(board))
