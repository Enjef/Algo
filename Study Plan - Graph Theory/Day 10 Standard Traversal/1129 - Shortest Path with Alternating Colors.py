class Solution:
    def shortestAlternatingPaths(
            self, n: int, redEdges: List[List[int]],
            blueEdges: List[List[int]]) -> List[int]:  # 41.52% 62.12%
        graph = {i: [[], []] for i in range(n)}
        for [i, j] in redEdges:
            graph[i][0].append(j)
        for [i, j] in blueEdges:
            graph[i][1].append(j)
        res = [float('inf') for _ in range(n)]
        res[0] = 0
        min_len = 0
        queue = deque()
        queue.append((0, 'r')) 
        queue.append((0, 'b')) 
        seen = set() 
        while queue:
            level_size = len(queue)
            min_len += 1
            for _ in range(level_size):
                node, color = queue.popleft()
                if (node, color) not in seen:
                    seen.add((node, color))
                    if color == 'r':
                        for child in graph[node][1]:
                            queue.append((child, 'b'))
                            res[child] = min(min_len, res[child])
                    if color == 'b':
                        for child in graph[node][0]:
                            queue.append((child, 'r'))
                            res[child] = min(min_len, res[child])
        for i in range(n):
            if res[i] == math.inf:
                res[i] = -1
        return res
