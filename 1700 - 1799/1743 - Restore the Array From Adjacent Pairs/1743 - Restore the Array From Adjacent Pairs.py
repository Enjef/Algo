class Solution:
    def restoreArray(self, adjacentPairs):  # 36.07% 72.27%
        edges = defaultdict(list)
        for first, second in adjacentPairs:
            edges[first].append(second)
            edges[second].append(first)
        stack = []
        for key in edges:
            if len(edges[key]) == 1:
                stack.append(key)
                break
        seen = set()
        result = []
        while stack:
            next_step = set()
            for cur in stack:
                if cur in seen:
                    continue
                seen.add(cur)
                result.append(cur)
                next_step.update(edges[cur])
            stack = next_step
        return result

    def restoreArray_best_speed(self, adjacentPairs):
        if adjacentPairs is None:
            return []
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
        start = 0
        for k in graph.keys():
            if len(graph[k]) == 1:
                start = k
                break
        queue = deque([start])
        visited = set([start])
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)
        return result

    def restoreArray_2nd_best_memory(self, adjacentPairs):
        d = defaultdict(list)
        for i, j in adjacentPairs:
            d[i].append(j)
            d[j].append(i)
        
        res = []
        for i in d:
            if len(d[i]) == 1:
                res.append(i)
                res.append(d[i][0])
                break
        while len(d[res[-1]]) != 1:
            if d[res[-1]][0] == res[-2]:
                res.append(d[res[-1]][1])
            else:
                res.append(d[res[-1]][0])
        return res
