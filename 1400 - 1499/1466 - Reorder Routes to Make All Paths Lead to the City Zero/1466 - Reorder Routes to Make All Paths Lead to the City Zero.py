class Solution:
    def minReorder(
            self, n: int, connections: List[List[int]]) -> int:  # 5.11% 93.02%
        seen = set([0])
        out = 0
        old = []
        while connections:
            start, finish = connections.pop()
            if finish in seen:
                seen.add(start)
            elif start in seen:
                seen.add(finish)
                out += 1
            else:
                old.append((start, finish))
            if not connections:
                connections = old
                old = []
        return out

    def minReorder_best_speed(
            self, n: int, connections: List[List[int]]) -> int:
        cmap = {0}
        count = 0
        dq = deque(connections)
        while dq:
            u, v = dq.popleft()
            if v in cmap:
                cmap.add(u)
            elif u in cmap:
                cmap.add(v)
                count += 1
            else:
                dq.append([u, v])
        return count
