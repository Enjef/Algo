class Solution:
    def findSmallestSetOfVertices(self, n, edges):  # 11.94% 5.02%
        ways = defaultdict(set)
        for start, end in edges:
            ways[start].add(end)
        seen = set()
        out = set()
        for i in range(n):
            if i in seen:
                continue
            out.add(i)
            stack = list(ways[i])
            while stack:
                next_row = set()
                for way in stack:
                    if way in seen:
                        continue
                    seen.add(way)
                    next_row.update(ways[way])
                stack = next_row
        return out - seen

    def findSmallestSetOfVertices_best_speed(self, n, edges):
        all_nodes = set(range(n))
        inbound_nodes = set()
        for _, v2 in edges:
            inbound_nodes.add(v2)
        return(all_nodes - inbound_nodes)

    def findSmallestSetOfVertices_best_memory(self, n, edges):
        hashMap = {}
        result = []
        for idx, edge in enumerate(edges):
            if edge[0] not in hashMap:
                hashMap[edge[0]] = 0
            if edge[1] not in hashMap:
                hashMap[edge[1]] = 1
            else:
                hashMap[edge[1]] += 1
        for key, value in hashMap.items():
            if value == 0:
                result.append(key)
        return result
