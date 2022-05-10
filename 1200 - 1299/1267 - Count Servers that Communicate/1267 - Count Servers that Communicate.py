class Solution:
    def countServers(self, grid: List[List[int]]) -> int:  # 54.63% 74.73%
        connected = set()
        for i, row in enumerate(grid):
            if sum(row) > 1:
                connected.update([(i, j) for j in range(len(row)) if row[j]])
        for i, col in enumerate(zip(*grid)):
            if sum(col) > 1:
                connected.update([(j, i) for j in range(len(col)) if col[j]])
        return len(connected)

    def countServers_best_speed(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = [0] * (m + n)
        mach = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    seen[i] += 1
                    seen[j + m] += 1
                    mach.append((i, j))
        result = 0   
        for i, j in mach:
            if seen[i] > 1 or seen[j + m] > 1:
                result += 1
        return result

    def countServers_2nd_best_speed(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = [0] * (m + n)
        mach = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    seen[i] += 1
                    seen[j + m] += 1
                    mach.append((i, j))
        result = 0   
        for i, j in mach:
            if seen[i] > 1 or seen[j + m] > 1:
                result += 1
        return result

    def countServers_best_memory(self, grid: List[List[int]]) -> int:
        servers = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    servers.add((i, j))
                    
        def isolated(i, j):
            nonlocal servers
            if any(filter(lambda x: x[0] == i and x != (i,j), servers)):
                return False
            if any(filter(lambda x: x[1] == j and x != (i,j), servers)):
                return False
            return True
            
        for server in list(servers):
            if isolated(*server):
                servers.remove(server)
        return len(servers)

    def countServers_2nd_best_memory(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        result = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if 1 in grid[i] or 1 in [v[j] for v in grid]:
                        result += 1
                    grid[i][j] = 1
        return result
