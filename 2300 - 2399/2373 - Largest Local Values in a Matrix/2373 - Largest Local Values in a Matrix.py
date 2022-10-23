class Solution:
    # 57.16% 87.53% (50.10% 43.73%)
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        ans = [[0]*(m-2) for _ in range(n-2)]
        for i in range(1, n-1):
            for j in range(1, m-1):
                ans[i-1][j-1] = max(
                    max(grid[i-1][j-1:j+2]),
                    max(grid[i][j-1:j+2]),
                    max(grid[i+1][j-1:j+2]))
        return ans


class Solution_best_speed:
    def largestLocal_1st(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid)
        ver_L = []
        out = []
        for _ in range(N-2):
            ver_L.append([])
            out.append([])
        for j in range(N):
            for i in range(N-2):
                ver_L[i].append(max(grid[j][i], grid[j][i+1], grid[j][i+2]))
        for L in ver_L:
            for i in range(len(L)-2):
                out[i].append(max(L[i], L[i+1], L[i+2]))
        return out

    def largestLocal_2nd(self, grid: List[List[int]]) -> List[List[int]]:
        length = len(grid)
        row, matrix, result = [], [], []
        for row in range(length):
            data = []
            for col in range(length - 2):
                data.append(max(grid[row][col:col+3]))
            matrix.append(data)
        for row in range(length - 2):
            data = []
            for col in range(length - 2):
                data.append(
                    max(matrix[row][col], matrix[row+1][col], matrix[row+2][col]))
            result.append(data)
        return result

    def largestLocal_3rd(self, grid: List[List[int]]) -> List[List[int]]:
        storage = [[0 for j in range(len(grid[i]) - 2)]
                   for i in range(len(grid) - 2)]
        for i in range(len(storage)):
            for j in range(len(storage[i])):
                rows = grid[i][j:j + 3] + \
                    grid[i + 1][j:j + 3] + grid[i + 2][j:j + 3]
                storage[i][j] = max(rows)
        return storage


class Solution_best_memory:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        rows = []
        for x_idx in range(n-2):
            row = []
            for y_idx in range(n-2):
                local = []
                for lx_idx in range(3):
                    for ly_idx in range(3):
                        x = x_idx + lx_idx
                        y = y_idx + ly_idx
                        local.append(grid[x][y])
                row.append(max(local))
            rows.append(row)
        return rows
