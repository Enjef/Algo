class Solution:
    # 97.23% 30.84% (99.88% 98.48%)
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = [-1] * n
        stack = [[i, i] for i in range(n)]
        i = 0
        while stack:
            new = []
            for ball, j in stack:
                cur = grid[i][j]
                if cur == 1:
                    if j < n-1 and grid[i][j+1] == 1:
                        new.append([ball, j+1])
                else:
                    if j > 0 and grid[i][j-1] == -1:
                        new.append([ball, j-1])
            i += 1
            if i == m:
                break
            stack = new
        for ball, j in new:
            res[ball] = j
        return res


class Solution_best_speed:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = [1] * n
        for start_col in range(n):
            row, col = 0, start_col
            for row in range(m):
                if grid[row][col] == 1:
                    if col + 1 < n and grid[row][col+1] == 1:
                        res[start_col] = col + 1
                        col += 1
                    else:
                        res[start_col] = -1
                        break
                else:
                    if col - 1 >= 0 and grid[row][col-1] == -1:
                        res[start_col] = col - 1
                        col -= 1
                    else:
                        res[start_col] = -1
                        break
        return res


class Solution_best_memory:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        re = [i for i in range(n)]
        for i in range(m-1, -1, -1):
            new_re = [0 for _ in range(n)]
            j = 0
            while j < n:
                if grid[i][j] == 1:
                    if j+1 < n and grid[i][j+1] == -1:
                        new_re[j] = -1
                        new_re[j+1] = -1
                        j += 2
                        continue
                    new_re[j] = re[j+1] if j+1 < n else -1
                else:
                    new_re[j] = re[j-1] if j-1 >= 0 else -1
                j += 1
            re = new_re
        return re
