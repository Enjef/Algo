class Solution:
    def isPathCrossing(self, path: str) -> bool:  # 95.26% 28.02%
        cur = [0, 0]
        step = [0, 0]
        visited = [cur]
        for direction in path:
            if direction == 'N':
                step = [1, 0]
            if direction == 'S':
                step = [-1, 0]
            if direction == 'E':
                step = [0, 1]
            if direction == 'W':
                step = [0, -1]
            cur = [x + y for x, y in zip(cur, step)]
            if cur in visited:
                return True
            visited.append(cur)
        return False

    def isPathCrossing_best_speed(self, path: str) -> bool:
        curr = (0, 0)
        seen = {curr}
        dirs = {'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)}
        for p in path:
            curr = (curr[0] + dirs[p][0], curr[1] + dirs[p][1])
            if curr in seen:
                return True
            seen.add(curr)
        return False
