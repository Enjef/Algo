class Solution:
    def findFarmland(self, land):  # 34.25% 27.30%
        def end_find(y, x):
            y_start, x_start = y, x
            while y < m and land[y][x]:
                y += 1
            while x < n and land[y-1][x]:
                x += 1
            for yy in range(y_start, y):
                for xx in range(x_start, x):
                    seen.add((yy, xx))
            return y-1, x-1

        out = []
        seen = set()
        m, n = len(land), len(land[0])
        for i in range(m):
            for j in range(n):
                if land[i][j] and (i, j) not in seen:
                    out.append([i, j, *end_find(i, j)])
        return out

    def findFarmland_best_speed(self, land):
        m = len(land)
        n = len(land[0])
        ans = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    if i > 0 and land[i-1][j] == 1:
                        continue
                    elif j > 0 and land[i][j-1] == 1:
                        continue
                    temp = [i, j]
                    k = i
                    while k+1 < m and land[k+1][j] == 1:
                        k += 1
                    temp.append(k)
                    k = j
                    while k+1 < n and land[i][k+1] == 1:
                        k += 1
                    temp.append(k)
                    ans.append(temp)
        return ans

    def findFarmland_best_memory(self, land):
        m = len(land)
        n = len(land[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(i, j):
            queue = [(i, j)]
            maxi, maxj = i, j
            while queue:
                length = len(queue)
                for _ in range(length):
                    k, l = queue.pop(0)
                    for x, y in moves:
                        ni, nj = k+x, l+y
                        if (
                            ni >= 0 and ni < m and nj >= 0 and
                            nj < n and not visited[ni][nj] and
                            land[ni][nj] == 1):
                                queue.append((ni, nj))
                                visited[ni][nj] = True
                                maxi, maxj = max(maxi, ni), max(maxj, nj)
            return (maxi, maxj)

        result = []
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and land[i][j] == 1:
                    visited[i][j] = True
                    mi, mj = bfs(i, j)
                    result.append((i, j, mi, mj))
        return result
