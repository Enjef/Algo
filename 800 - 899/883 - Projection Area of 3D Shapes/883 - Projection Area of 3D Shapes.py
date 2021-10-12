class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:  # 86.96% 24.64%
        xy_area = sum([1 if x else 0 for tup in grid for x in tup])
        yz_area = sum(max(tup) for tup in grid)
        zx_area = sum([max(tup) for tup in zip(*grid)])
        return xy_area + yz_area + zx_area

    def projectionArea_best_speed_short(
            self,
            grid: List[List[int]]) -> int:  # 94.93% 6.52%
        hor = sum(map(max, grid))
        ver = sum(map(max, zip(*grid)))
        top = sum(v > 0 for row in grid for v in row)
        return ver + hor + top

    def projectionArea_best_memory(
            self,
            grid: List[List[int]]) -> int:  # 17.39% 56.88%
        ans = 0
        n = len(grid)
        rmax = [0] * n
        cmax = [0] * n
        for x in range(n):
            for y in range(n):
                rmax[x] = max(rmax[x], grid[x][y])
                cmax[y] = max(cmax[y], grid[x][y])
                if grid[x][y] > 0:
                    ans += 1
        return ans + sum(rmax) + sum(cmax)
