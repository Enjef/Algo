class Solution:
    def numOfMinutes(self, n, headID, manager, informTime):  # 43.95% 86.96%
        layers = defaultdict(list)
        for i in range(n):
            layers[manager[i]].append(i)
        res = 0
        stack = [(-1, 0)]
        while stack:
            next_row = set()
            for el, cur_time in stack:
                if el not in layers:
                    res = max(res, cur_time)
                    continue
                next_row.update(
                    tuple((x, cur_time+informTime[x])) for x in layers[el]
                )
            stack = next_row
        return res
