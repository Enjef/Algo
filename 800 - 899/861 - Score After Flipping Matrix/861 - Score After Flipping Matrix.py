class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:  # 48.50% 94.36%
        n, m = len(grid), len(grid[0])
        for i in range(n):
            if grid[i][0] == 0:
                for j in range(m):
                    grid[i][j] ^= 1
        for i, col in enumerate(zip(*grid)):
            if i == 0:
                continue
            if sum(col) <= n // 2:
                for j in range(n):
                    grid[j][i] ^= 1
        return sum(int(''.join(map(str, x)), 2) for x in grid)

    def matrixScore_best_speed(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            if grid[i][0] == 0:
                for j in range(len(grid[0])):
                    grid[i][j] = 1 if grid[i][j] == 0 else 0
        thres = len(grid) // 2
        count = 0
        for j in range(1, len(grid[0])):
            count = 0
            for i in range(len(grid)):
                if grid[i][j] == 1:
                    count += 1
            if count < thres + 1:
                for i in range(len(grid)):
                    grid[i][j] = 1 if grid[i][j] == 0 else 0
        res = 0
        for i in range(len(grid)):
            curr = ''
            for j in range(len(grid[0])):
                curr += str(grid[i][j])
            res += int(curr, 2)
        return res

    def matrixScore_2nd_best_speed(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        change = [0]*len(grid)
        for i in range(m):
            if grid[i][0] == 0:
                change[i] = 1
        ans = 0
        for j in range(len(grid[0])):
            one, zero = 0, 0
            for i in range(len(grid)):
                if abs(grid[i][j] - change[i]):
                    one += 1
                else:
                    zero += 1
            ans = ans*2+max(one, zero)
        return ans

    def matrixScore_best_memory(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        for i in range(n):
            if grid[i][0] == 0:
                for j in range(m):
                    grid[i][j] = 0 if grid[i][j] == 1 else 1
        store = [0]*m
        for i in range(m):
            for j in range(n):
                if grid[j][i] == 0:
                    store[i] += 1
        for i in range(m):
            if store[i] > n//2:
                for j in range(n):
                    grid[j][i] = 0 if grid[j][i] == 1 else 1
        res = 0
        for i in range(n-1, -1, -1):
            temp = 0
            for j in range(m-1, -1, -1):
                temp += grid[i][j]*(1 << (m-1-j))
            res += temp
        return res
