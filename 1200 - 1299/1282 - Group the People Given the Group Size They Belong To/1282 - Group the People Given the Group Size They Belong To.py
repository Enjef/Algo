class Solution:
    def groupThePeople_my(self, groupSizes):  # 73.44%
        if len(groupSizes) == 1:
            return [[0]]
        g_map = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] in g_map:
                g_map[groupSizes[i]].append(i)
            else:
                g_map[groupSizes[i]] = [i]
        out = []
        for i in g_map:
            block = len(g_map[i]) // i
            if block > 1:
                for _ in range(block):
                    out.append([g_map[i].pop() for _ in range(i)])
            else:
                out.append([g_map[i].pop() for _ in range(i)])
        return out

    def groupThePeople_best(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}
        for i, n in enumerate(groupSizes):
            if n not in d:
                d[n] = [[]]
            if len(d[n][-1]) == n:
                d[n] += [[]]
            d[n][-1] += [i]
        return sum(d.values(), [])
