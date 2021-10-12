class Solution:
    def allCellsDistOrder(
            self,
            rows: int,
            cols: int,
            rCenter: int,
            cCenter: int) -> List[List[int]]:  # 95.24% 74.07%
        distance = {}
        for i in range(rows):
            for j in range(cols):
                temp = abs(i-rCenter) + abs(j-cCenter)
                if temp not in distance:
                    distance[temp] = []
                distance[temp].append([i, j])
        return [y for x in sorted(distance.keys()) for y in distance[x]]

    def allCellsDistOrder_best(
            self,
            rows: int,
            cols: int,
            rCenter: int,
            cCenter: int) -> List[List[int]]:
        max_diff = rows + cols - 2
        default_d = defaultdict(list)
        res = []
        for i in range(rows):
            for j in range(cols):
                distance = abs(i - rCenter) + abs(j - cCenter)
                default_d[distance].append([i, j])
        for i in range(max_diff + 1):
            if i in default_d:
                res.extend(default_d[i])
        return res
