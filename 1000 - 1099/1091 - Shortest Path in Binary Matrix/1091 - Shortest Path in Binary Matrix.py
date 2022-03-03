class Solution:
    def shortestPathBinaryMatrix(self, grid):  # 69.85% 77.05%
        stack = [(0, 0)]
        n = len(grid)
        r_dir = [-1, -1, -1, 0, 0, 1, 1, 1]
        c_dir = [-1, 0, 1, -1, 1, -1, 0, 1]
        cur = 1
        while stack:
            temp = []
            while stack:
                row, col = stack.pop()
                if not(-1<row<n and -1<col<n) or grid[row][col]:
                    continue
                grid[row][col] = 1
                if (row, col) == (n-1, n-1):
                    return cur
                for idx in range(8):
                    temp.append((row+r_dir[idx], col+c_dir[idx]))
            stack = temp
            cur += 1
        return -1

    def shortestPathBinaryMatrix_best_speed(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        m, n = len(grid), len(grid[0])
        pq = [(max(m, n), 1, m - 1, n - 1)]
        while pq:
            _, length, i, j = heapq.heappop(pq)
            if i == 0 and j == 0:
                return length
            for ni, nj in [(i + 1, j), (i + 1, j - 1), (i, j - 1), (i - 1, j - 1), \
                           (i - 1, j), (i - 1, j + 1), (i, j + 1), (i + 1, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and (grid[ni][nj] == 0 or -grid[ni][nj] > length):
                    heapq.heappush(pq, (length + max(ni, nj), length + 1, ni, nj))
                    grid[ni][nj] = -length
        return -1


class Solution_2nd_best_speed:
    def __init__(self):
        self.DIRECTIONS = [
            (-1, -1), (0, -1), (1, -1),
            (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        max_row, max_col = len(grid), len(grid[0])
        if max_row == 1 and max_col == 1:
            return 1
        goal = (max_row - 1, max_col - 1)
        forward_queue = set([(0, 0)])
        backward_queue = set([goal])
        visited = [[0] * max_col for _ in range(max_row)]
        visited[0][0], visited[-1][-1] = 1, 1
        steps = 1
        while forward_queue and backward_queue:
            steps += 1
            next_queue = set()
            for row, col in forward_queue:           
                for dr, dc in self.DIRECTIONS:
                    new_row, new_col = row + dr, col + dc
                    if (
                        new_row < 0 or new_row >= max_row or
                        new_col < 0 or new_col >= max_col):
                            continue
                    if (new_row, new_col) in backward_queue:
                        return steps
                    if visited[new_row][new_col] or grid[new_row][new_col] == 1:
                        continue
                    visited[new_row][new_col] = 1
                    next_queue.add((new_row, new_col))
            if len(next_queue) <= len(backward_queue):
                forward_queue = next_queue
            else:
                forward_queue = backward_queue
                backward_queue = next_queue
        return -1
