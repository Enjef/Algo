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

    def exist_v2(
            self,
            board: List[List[str]],
            word: str) -> bool:  # 46.42% 72.72%
        def checker(x, y, visited, ind=0, res=[False]):
            visited.append((x, y))
            if ind == z-1 and board[x][y] == word[ind]:
                res[0] = True
                return res[0]
            for xx, yy in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if (
                        xx < 0 or yy < 0 or
                        xx > m - 1 or yy > n - 1 or
                        board[xx][yy] != word[ind+1] or
                        (xx, yy) in visited):
                    continue
                checker(xx, yy, visited[:], ind+1, res)
            return res[0]
        m = len(board)
        n = len(board[0])
        z = len(word)
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and checker(i, j, [], 0, [False]):
                    return True
        return False

     def exist_v2_refactored(
            self,
            board: List[List[str]],
            word: str) -> bool:  # 49.26% 45.83%
        def checker(x, y, visited, ind=0):
            res = False
            visited.append((x, y))
            if ind == z-1 and board[x][y] == word[ind]:
                return True
            for xx, yy in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if (
                        xx < 0 or yy < 0 or xx > m - 1 or yy > n - 1 or
                        board[xx][yy] != word[ind+1] or (xx, yy) in visited):
                    continue
                res = res or checker(xx, yy, visited[:], ind+1)
            return res
        m = len(board)
        n = len(board[0])
        z = len(word)
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and checker(i, j, [], 0):
                    return True
        return False
