class Solution:
    # 66.16% 52.53% (72.13% 78.41%)
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols = list(zip(*grid))
        count = Counter(cols)
        res = 0
        for row in grid:
            cur = tuple(row)
            if cur in cols:
                res += count[cur]
        return res


class Solution_best_speed:
    def equalPairs(self, grid: List[List[int]]) -> int:
        seen = Counter(tuple(row) for row in grid)
        return sum(seen[tuple(column)] for column in zip(*grid))


class Solution_best_memory:
    def equalPairs(self, grid: List[List[int]]) -> int:
        Column = []
        for i in range(len(grid)):
            temp = []
            for j in range(len(grid)):
                temp.append(grid[j][i])
            Column.append(temp)
        result = 0
        for k in Column:
            result += grid.count(k)
        return result
