class Solution:
    def validPath(
            self, n: int, edges: List[List[int]],
            source: int, destination: int) -> bool:  # 25.09% 32.64%
        ways = defaultdict(set)
        for start, end in edges:
            ways[start].add(end)
            ways[end].add(start)
        seen = set()
        stack = ways[source]
        while stack:
            new = set()
            for cur in stack:
                if cur in seen:
                    continue
                if cur == destination:
                    return True
                seen.add(cur)
                new.update(ways[cur])
            stack = new
        return False

    def validPath_v2(
            self, n: int, edges: List[List[int]],
            source: int, destination: int) -> bool:  # 12.80% 34.58%
        ways = defaultdict(set)
        for start, end in edges:
            ways[start].add(end)
            ways[end].add(start)
        seen = set()
        stack = [source]
        while stack:
            new = set()
            for cur in stack:
                if cur in seen:
                    continue
                if cur == destination:
                    return True
                seen.add(cur)
                new.update(ways[cur])
            stack = new
        return False

    def validPath_v3(
            self, n: int, edges: List[List[int]],
            source: int, destination: int) -> bool:  # 30.82% 5.13%
        def dfs(node):
            if node in seen:
                return False
            if node == destination:
                return True
            result = False
            seen.add(node)
            for sub in ways[node]:
                result |= dfs(sub)
            return result

        ways = defaultdict(set)
        for start, end in edges:
            ways[start].add(end)
            ways[end].add(start)
        seen = set()
        return dfs(source)

    def validPath_best_speed(
            self, n: int, edges: List[List[int]],
            source: int, destination: int) -> bool:
        if source == destination:
            return True
        visited = set([source])
        stepped = True
        while stepped:
            stepped = False
            for a, b in edges:
                if a in visited and b in visited:
                    continue
                if a in visited or b in visited:
                    if destination in [a, b]:
                        return True
                    stepped = True
                    visited.update([a, b])
        return False


def parent(node, parents):
    if parents[node] is None:
        return node
    return parent(parents[node], parents)


def unionFind(edges, parents):
    if len(edges) == 0:
        return
    check = edges.pop()
    a = parent(check[0], parents)
    b = parent(check[1], parents)
    if a == b:
        pass
    else:
        parents[a] = b


class Solution_best_memory:
    def validPath(
            self, n: int, edges: List[List[int]],
            source: int, destination: int) -> bool:
        parents = [None for i in range(n)]
        while len(edges) > 0:
            unionFind(edges, parents)
        return parent(source, parents) == parent(destination, parents)
