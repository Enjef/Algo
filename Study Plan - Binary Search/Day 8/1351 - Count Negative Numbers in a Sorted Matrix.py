class Solution:
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
