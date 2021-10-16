class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:  # 56.73% 37.71%
        m = len(grid)
        n = len(grid[0])
        time = 0
        fresh = []
        rotten = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh.append((i, j))
                if grid[i][j] == 2:
                    rotten.append((i, j))
        while rotten:
            new_rotten = []
            while rotten:
                i, j = rotten.pop()
                for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if (x, y) in fresh:
                        fresh.remove((x, y))
                        new_rotten.append((x, y))
            if new_rotten:
                time += 1
            rotten = new_rotten
        return -1 if fresh else time

    def orangesRotting_two(self, grid: List[List[int]]) -> int:  # 90.97% 9.23%
        m = len(grid)
        n = len(grid[0])
        time = 0
        fresh = []
        rotten = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh.append((i, j))
                if grid[i][j] == 2:
                    rotten.append((i, j))
        while rotten:
            new_rotten = []
            while rotten:
                i, j = rotten.pop()
                for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if x < 0 or y < 0 or x > m - 1 or y > n - 1:
                        continue
                    if (x, y) in fresh:
                        fresh.remove((x, y))
                        new_rotten.append((x, y))
            if new_rotten:
                time += 1
            rotten = new_rotten
        return -1 if fresh else time
