class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        ways = defaultdict(list)
        for start, end in roads:
            ways[start].append(end)
            ways[end].append(start)
        values = dict(
            zip(
                sorted(ways, key=lambda x: len(ways[x]), reverse=True),
                range(n,-1,-1)
            ))
        seen = set()
        total = 0
        for val in sorted(values, key=values.get, reverse=True):
            if val in seen:
                continue
            seen.add(val)
            for node in ways[val]:
                if node in seen:
                    continue
                total += values[val] + values[node]
        return total
