import collections


class Solution:
    # 37.71% 81.20% (28.77% 70.43%)
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        nodes = defaultdict(list)
        restricted = set(restricted)
        for i, j in edges:
            nodes[i].append(j)
            nodes[j].append(i)
        stack = [0]
        res = 0
        seen = set()
        while stack:
            new = set()
            for node in stack:
                if node in restricted or node in seen:
                    continue
                res += 1
                seen.add(node)
                new.update(nodes[node])
            stack = new
        return res


class Solution_best_speed:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        def bfs(x):
            q = collections.deque([x])
            visited = [0] * n
            visited[x] = 1
            cnt = 0
            while q:
                x = q.popleft()
                cnt += 1
                for next_node in graph[x]:
                    if not visited[next_node]:
                        q.append(next_node)
                        visited[next_node] = 1
            return cnt

        graph = [[]*n for _ in range(n)]
        restricted = set(restricted)
        for x, y in edges:
            if x not in restricted and y not in restricted:
                graph[x].append(y)
                graph[y].append(x)
        return bfs(0)


class Solution_best_memory:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        hashmap = {}
        for edge in edges:
            if edge[0] not in hashmap:
                hashmap[edge[0]] = []
            hashmap[edge[0]].append(edge[1])
            if edge[1] not in hashmap:
                hashmap[edge[1]] = []
            hashmap[edge[1]].append(edge[0])
        q = collections.deque()
        q.append(0)
        ret = 1
        seen = set(restricted)
        seen.add(0)
        while q:
            curr = q.popleft()
            for node in hashmap[curr]:
                if node not in seen:
                    ret += 1
                    seen.add(node)
                    q.append(node)
        return ret
