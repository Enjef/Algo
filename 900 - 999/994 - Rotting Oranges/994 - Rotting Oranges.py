class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:  # 11.18% 41.06%
        m, n = len(grid), len(grid[0])
        time = 0
        fresh = set()
        rotten = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                if grid[i][j] == 2:
                    rotten.add((i, j))
        while fresh:
            if not rotten:
                return -1
            new = set()
            while rotten:
                i, j = rotten.pop()
                new.update([(i-1, j), (i+1, j), (i, j-1), (i, j+1)])
            rotten = fresh & new
            fresh -= rotten
            if rotten:
                time += 1
        return time

    def orangesRotting(self, grid: List[List[int]]) -> int:  # 68.30% 41.06%
        time = 0
        fresh = set()
        rotten = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                if grid[i][j] == 2:
                    rotten.add((i, j))
        while rotten and fresh:
            new = set()
            while rotten:
                i, j = rotten.pop()
                for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if (x, y) not in fresh:
                        continue
                    new.add((x, y))
                    fresh.remove((x, y))
            rotten = new
            time += 1
        return -1 if fresh else time

    def orangesRotting_best_speed(self, grid: List[List[int]]) -> int: 
        visit, curr = set(), deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    visit.add((i, j))
                elif grid[i][j] == 2:
                    curr.append((i, j))
        result = 0
        while visit and curr:
            for _ in range(len(curr)):
                i, j = curr.popleft()
                for coord in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if coord in visit:
                        visit.remove(coord)
                        curr.append(coord)
            result += 1
        return -1 if visit else result
