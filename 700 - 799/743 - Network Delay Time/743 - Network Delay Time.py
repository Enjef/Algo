class Solution:
    def networkDelayTime(self, times, n, k):  # 44.55% 92.16%
        nodes = defaultdict(list)
        for start, end, time in times:
            nodes[start].append((end, time))
        seen = set()
        arr = [(0, k)]
        while arr:
            time, node = heappop(arr)
            seen.add(node)
            if len(seen) == n:
                return time
            for cur_target, cur_time in nodes[node]:
                if cur_target not in seen:
                    heappush(arr, (time+cur_time, cur_target))
        return -1

    def networkDelayTime_best_speed(
            self, times: List[List[int]], n: int, k: int) -> int:
        d = {x: float('inf') for x in range(1, n + 1)}
        adj_list = {x: [] for x in range(1, n + 1)}
        d[k] = 0
        for u, v, w in times:
            adj_list[u].append((v, w))
        min_heap = [(0, k)]
        while min_heap:
            weight, vertex = heapq.heappop(min_heap)
            if d[vertex] != weight:
                continue
            neighbors = adj_list[vertex]
            for v, w in neighbors:
                new_weight = w + weight
                if d[v] > new_weight:
                    d[v] = new_weight
                    heapq.heappush(min_heap, (new_weight, v))
        if max(d.values()) == float('inf'):
            return -1
        else:
            return max(d.values())

    def networkDelayTime_best_memory(
            self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for record in times:
            u = record[0]
            v = record[1]
            w = record[2]
            edges[u].append([v, w])
        minDelays = [float("inf")] * n
        minDelays[k - 1] = 0
        stack = [k]
        while stack:
            u = stack.pop()
            for v, w in edges[u]:
                if minDelays[u - 1] + w < minDelays[v - 1]:
                    minDelays[v - 1] = minDelays[u - 1] + w
                    stack.append(v)
        for delay in minDelays:
            if delay == float("inf"):
                return -1
        return max(minDelays)
