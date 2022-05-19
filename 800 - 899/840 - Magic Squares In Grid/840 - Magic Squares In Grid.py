class Solution:
    def numMagicSquaresInside(
            self, grid: List[List[int]]) -> int:  # 80.29% 14.60%
        def check(x, y):
            complete = set()
            tested = []
            for xx in range(x, x+3):
                for yy in range(y, y+3):
                    complete.add(grid[xx][yy])
            tested.extend([sum(row[y:y+3]) for row in grid[x:x+3]])
            tested.extend([sum(col) for col in zip(*grid[x:x+3])][y:y+3])
            tested.append(sum([grid[x+i][y+i] for i in range(3)]))
            tested.append(sum([grid[2+x-i][y+i] for i in range(3)]))
            if complete != set(range(1, 10)):
                return False
            for i in range(1, len(tested)):
                if tested[i] != tested[i-1]:
                    return False
            return True

        m, n = len(grid), len(grid[0])
        if m < 3 or n < 3:
            return 0
        result = 0
        for i in range(m-2):
            for j in range(n-2):
                result += check(i, j)
        return result


class Solution_best_memory:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        ans = 0
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                if grid[i][j] == 5:
                    new_grid = []
                    for m in range(i-1, i+2):
                        for n in range(j-1, j+2):
                            new_grid.append(grid[m][n])
                    if self.ismagic(new_grid) == True:
                        ans = ans + 1
        return ans

    def ismagic(self, grid):
        if len(set(grid)) != 9:
            return False
        if max(grid) != 9 or min(grid) != 1:
            return False
        col = [0]*3
        lin = [0]*3
        for i in range(len(grid)):
            col[i % 3] = col[i % 3] + grid[i]
            lin[i//3] = lin[i//3] + grid[i]
        if len(set(col)) != 1 or len(set(lin)) != 1:
            return False
        return True
