class Solution:
    # 66.67% 88.89% (20.90% 88.89%)
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        def helper(x, y):
            xx = x - 1
            while xx > -1 and ((x, y) == (xx, y) or (xx, y) not in guard) and (xx, y) not in wall:
                guarded.add((xx, y))
                xx -= 1
            yy = y - 1
            while yy > -1 and ((x, y) == (x, yy) or (x, yy) not in guard) and (x, yy) not in wall:
                guarded.add((x, yy))
                yy -= 1
            xx = x + 1
            while xx < m and ((x, y) == (xx, y) or (xx, y) not in guard) and (xx, y) not in wall:
                guarded.add((xx, y))
                xx += 1
            yy = y + 1
            while yy < n and ((x, y) == (x, yy) or (x, yy) not in guard) and (x, yy) not in wall:
                guarded.add((x, yy))
                yy += 1
            return

        guard = {(x, y) for x, y in guards}
        wall = {(x, y) for x, y in walls}
        guarded = set()
        for i in range(m):
            for j in range(n):
                if (i, j) in guard:
                    helper(i, j)
        return m * n - len(guard) - len(wall) - len(guarded)

    # 84.89% 94.22% (32.89% 88.89%)
    def countUnguarded_v2(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        def helper(x, y):
            xx = x - 1
            while xx > -1 and (xx, y) not in guard and (xx, y) not in wall:
                guarded.add((xx, y))
                xx -= 1
            yy = y - 1
            while yy > -1 and (x, yy) not in guard and (x, yy) not in wall:
                guarded.add((x, yy))
                yy -= 1
            xx = x + 1
            while xx < m and (xx, y) not in guard and (xx, y) not in wall:
                guarded.add((xx, y))
                xx += 1
            yy = y + 1
            while yy < n and (x, yy) not in guard and (x, yy) not in wall:
                guarded.add((x, yy))
                yy += 1
            return

        guard = {(x, y) for x, y in guards}
        wall = {(x, y) for x, y in walls}
        guarded = set()
        for i in range(m):
            for j in range(n):
                if (i, j) in guard:
                    helper(i, j)
        return m * n - len(guard) - len(wall) - len(guarded)


class Solution_best_speed:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for i, j in walls + guards:
            grid[i][j] = 1

        for i, j in guards:
            x = i + 1
            while x < m and grid[x][j] != 1:
                grid[x][j] = 2
                x += 1
            x = i - 1
            while x >= 0 and grid[x][j] != 1:
                grid[x][j] = 2
                x -= 1
            y = j + 1
            while y < n and grid[i][y] != 1:
                grid[i][y] = 2
                y += 1
            y = j - 1
            while y >= 0 and grid[i][y] != 1:
                grid[i][y] = 2
                y -= 1
        output = 0
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    output += 1
        return output


class Solution_best_memory:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        dp = [[0] * n for _ in range(m)]
        for x, y in guards+walls:
            dp[x][y] = 1
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for x, y in guards:
            for dx, dy in directions:
                curr_x = x
                curr_y = y
                while 0 <= curr_x+dx < m and 0 <= curr_y+dy < n and dp[curr_x+dx][curr_y+dy] != 1:
                    curr_x += dx
                    curr_y += dy
                    dp[curr_x][curr_y] = 2
        return sum(1 for i in range(m) for j in range(n) if dp[i][j] == 0)
