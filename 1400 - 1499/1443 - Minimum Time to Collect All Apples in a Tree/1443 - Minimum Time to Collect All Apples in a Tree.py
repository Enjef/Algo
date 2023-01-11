class Solution:
    # 71.80% 47.44% (71.80% 33.33%)
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(node):
            cur = 0
            self.seen.add(node)
            if node in self.root:
                for child in self.root[node]:
                    if child not in self.seen:
                        cur += dfs(child)
            if node and (cur or int(hasApple[node])):
                cur += 1
            return cur

        self.seen = set()
        self.root = defaultdict(list)
        for x, y in edges:
            self.root[x].append(y)
            self.root[y].append(x)
        return dfs(0) * 2


class Solution_best_speed:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(parent, node):
            steps = 0
            for c in graph[node]:
                if c != parent:
                    steps += dfs(node, c)
            if (hasApple[node] or steps > 0) and node != 0:
                steps += 2
            return steps

        return dfs(-1, 0)

    def minTime_2nd_best(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(node: int, prev: int) -> bool:
            for neighbor in graph[node]:
                if neighbor != prev and dfs(neighbor, node):
                    hasApple[node] = True
            return hasApple[node]

        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        dfs(0, -1)
        return (sum(hasApple) - hasApple[0]) * 2


class Solution_best_memory:
    @staticmethod
    def dfs(tree, seed, has, parent):
        time = 0
        count = 0
        if has[seed]:
            count += 1
        for child in tree[seed]:
            if parent == child:
                continue
            t, c = Solution.dfs(tree, child, has, seed)
            count += c
            if c > 0:
                time += t + 2
        return time, count

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = [([]) for _ in range(n)]
        for edge in edges:
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])
        t, _ = Solution.dfs(tree, 0, hasApple, -1)
        return t


class Solution_second_best_memory:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int: 
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(par, cur):
            nonlocal n, adj
            apple = hasApple[cur]
            for nxt in adj[cur]:
                if nxt != par:
                    apple |= dfs(cur, nxt)
            if not apple:
                n -= 1
            return apple

        dfs(-1, 0)
        return max(0, (n-1) * 2)
