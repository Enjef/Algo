class Solution:
    def findJudge(self, n: int, trust):  # 69.58% 91.83%
        if not trust:
            if n == 1:
                return 1
            else:
                return -1
        town = defaultdict(set)
        for start, end in trust:
            town[start].add(end)
        out = set.intersection(*town.values()) - set(town)
        if not out or len(town) < n-1:
            return -1
        out = out.pop()
        return out if out not in town else -1
