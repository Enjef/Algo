class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:  # 81.21%  47.11%
        out = 0
        for row in grid:
            for i in range(len(row)):
                if row[i] < 0:
                    out += len(row[i:])
                    break
        return out

    def countNegatives_v2(self, grid):  # 89.68% 80.90%
        n, m = len(grid), len(grid[0])
        cnt = 0
        row = n-1
        col = 0
        while(row >= 0 and col < m):
            if grid[row][col] < 0:
                cnt += m - col
                row -= 1
                col = 0
            else:
                col += 1
        return cnt

    def countNegatives_short(self, grid: List[List[int]]) -> int:
        return sum(x < 0 for row in grid for x in row)

    def countNegatives_study(self, grid):  # 44.97% 97.77%
        def bin_search(idx):
            left, right = 0, n
            while left < right:
                mid = left + (right-left)//2
                if grid[idx][mid] < 0:
                    right = mid
                else:
                    left = mid + 1
            return right

        down = m = len(grid)-1
        n = len(grid[0])-1
        up = 0
        out = 0
        while up <= down:
            mid = up + (down-up)//2
            if grid[mid][-1] < 0:
                down = mid - 1
            else:
                up = mid + 1
        for i in range(up, m+1):
            out += n - bin_search(i) + 1
        return out

    def countNegatives_best_speed(self, grid: List[List[int]]) -> int:
        numneg = 0
        for g in grid:
            left = 0
            right = len(g)-1

            while left < right:
                mid = (left+right)//2
                if g[mid] >= 0:
                    left = mid+1
                else:
                    right = mid
            if g[left] < 0:
                numneg += (len(g)-1-left+1)
        return numneg

    def countNegatives_2nd_best_speed(self, grid: List[List[int]]) -> int:
        i, count, m, n = 0, 0, len(grid)-1, len(grid[0])-1
        while i <= m and n >= 0:
            if grid[i][n] < 0:
                count = count+(m+1-i)
                n = n-1
            else:
                i = i+1
        return count

    def countNegatives_best_memory(self, n: List[List[int]]) -> int:
        q = 0
        for i in range(len(n)-1, -1, -1):
            if n[i][len(n[i])-1] >= 0:
                break
            for j in range(len(n[i])-1, -1, -1):
                if n[i][j] < 0:
                    q += 1
                else:
                    break
        return q
