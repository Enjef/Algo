class Solution:
    def countBattleships(
            self,
            board: List[List[str]]) -> int:  # 77.33%  92.35%
        total = len(board) * len(board[0])

        def checker(ind_m, ind_n):
            if (
                    0 <= ind_m <= len(board)-1 and
                    0 <= ind_n <= len(board[0])-1 and
                    board[ind_m][ind_n] == 'X'):
                return True
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (
                        board[i][j] == '.' or
                        board[i][j] != '.' and (
                            checker(i-1, j) or checker(i, j-1))):
                    total -= 1
        return total

    def countBattleships_best_speed(self, board: List[List[str]]) -> int:
        n, m = len(board), len(board[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == '.':
                    continue
                up_i, up_j = i-1, j
                left_i, left_j = i, j-1
                if up_i >= 0 and board[up_i][up_j] == 'X':
                    continue
                if left_j >= 0 and board[left_i][left_j] == 'X':
                    continue
                count += 1
        return count

    def countBattleships_best_memory(self, board: List[List[str]]) -> int:
        m = len(board)
        if m == 0:
            return 0
        n = len(board[0])
        res = 0
        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == '.':
                    continue
                left, up = False, False
                if i == 0 or board[i-1][j] == '.':
                    left = True
                if j == 0 or board[i][j-1] == '.':
                    up = True
                if left and up:
                    res += 1
        return res
