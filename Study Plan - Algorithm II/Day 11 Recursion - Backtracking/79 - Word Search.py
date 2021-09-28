class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:  # 5.00% 41.52%
        def checker(i, j, word, seen=[]):
            if (
                    (i, j) in seen or
                    not(0 <= i < len(board) and 0 <= j < len(board[0])) or
                    board[i][j] != word[0]):
                return False
            if board[i][j] == word:
                return True
            seen.append((i, j))
            return (
                checker(i-1, j, word[1:], seen[:]) or
                checker(i+1, j, word[1:], seen[:]) or
                checker(i, j-1, word[1:], seen[:]) or
                checker(i, j+1, word[1:], seen[:])
            )
        for i in range(len(board)):
            for j in range(len(board[0])):
                if checker(i, j, word, []):
                    return True
        return False
