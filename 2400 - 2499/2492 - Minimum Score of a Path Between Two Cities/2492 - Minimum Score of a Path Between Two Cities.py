from collections import deque, defaultdict


# 13.75% 5.03% (15.10% 5.03%)
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        nodes = [[] for _ in range(n+1)]
        seen = defaultdict(list)
        for x, y, weight in roads:
            nodes[x].append((y, weight))
            nodes[y].append((x, weight))
        seen = {x: float('inf') for x in range(1, n+1)}
        queue = deque([(1, 100001)])
        result = 100001
        while queue:
            node, way = queue.popleft()
            if seen[node] <= way:
                continue
            seen[node] = way
            if node == n:
                result = min(result, seen[node])
            for child, cost in nodes[node]:
                queue.append((child, min(way, cost)))
        return result


class Solution_best_speed:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        d = defaultdict(list)
        for i, j, _ in roads:
            d[i].append(j)
            d[j].append(i)
        seen = set()
        l = deque([1])
        while l:
            x = l.popleft()
            for i in d[x]:
                if i not in seen:
                    l.append(i)
                    seen.add(i)
        res = 1000000
        for i, j, d in roads:
            if i in seen or j in seen:
                res = min(res, d)
        return res


class Solution_2nd_best_speed:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        q = deque(roads)
        pool = {1, n}
        re = 10**4+1
        while q:
            lth = len(q)
            for _ in range(len(q)):
                temp = q.popleft()
                if temp[0] in pool or temp[1] in pool:
                    re = min(re, temp[2])
                    pool.add(temp[0])
                    pool.add(temp[1])
                else:
                    q.append(temp)
            if lth == len(q):
                break
        return re


class Solution_best_memory:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        partition = {1, n}
        result = None
        fruitfulPass = True
        while fruitfulPass and len(roads) > 0:
            fruitfulPass = False
            used = []
            for ri, road in enumerate(roads):
                node1, node2, score = road
                found = False
                if node1 in partition:
                    nodeX = node2
                    found = True
                elif node2 in partition:
                    nodeX = node1
                    found = True
                if found:
                    partition.add(nodeX)
                    if result is None or result > score:
                        result = score
                    used += [ri]
                    fruitfulPass = True
            for i, re in enumerate(used):
                del roads[re-i]
        return result
