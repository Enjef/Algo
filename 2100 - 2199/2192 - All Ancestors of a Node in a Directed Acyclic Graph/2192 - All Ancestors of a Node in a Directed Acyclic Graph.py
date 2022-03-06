class Solution:
    def getAncestors(self, n: int, edges):  # 22.22% 22.22%
        def dfs(idx, cur):
            if idx in mem:
                return mem[idx]
            cur = set()
            if idx in ways:
                for way in ways[idx]:
                    if way in ways:
                        cur.update(dfs(way, cur.copy()))
                    cur.add(way)
            mem[idx] = cur
            return mem[idx]
        
        ways = {}
        mem = {}
        for first, second in edges:
            if second not in ways:
                ways[second] = []
            ways[second].append(first)
        for i in range(n):
            dfs(i,set())
        return [sorted(mem[i])for i in range(n)]

    def getAncestors_v2(self, n: int, edges):  # 44.44% 22.22%
        def dfs(idx):
            if idx in mem:
                return mem[idx]
            cur = set()
            if idx in ways:
                for way in ways[idx]:
                    if way in ways:
                        cur.update(dfs(way))
                    cur.add(way)
            mem[idx] = cur
            return mem[idx]
        
        ways = {}
        mem = {}
        for first, second in edges:
            if second not in ways:
                ways[second] = set()
            ways[second].add(first)
        arr = []
        for i in range(n):
            arr.append(sorted(dfs(i)))
        return arr

    def getAncestors_v3_stack(self, n, edges):  # 11.11% 100.00%
        ways = {}
        mem = {}
        for first, second in edges:
            if second not in ways:
                ways[second] = set()
            ways[second].add(first)
        arr = []
        for i in range(n):
            way = set()
            stack = [i]
            while stack:
                temp = set()
                while stack:
                    cur = stack.pop()
                    if cur in mem:
                        way.update(mem[cur])
                        continue
                    if cur not in ways:
                        continue
                    temp.update(ways[cur])
                    way.update(ways[cur])
                stack = temp
            mem[i] = sorted(way)
            arr.append(mem[i])
        return arr

    def getAncestors_best_speed(self, n, edges):
        graph = [[] for _ in range(n)]
        ind = [0] * n
        for u, v in edges:
            graph[u].append(v)
            ind[v] += 1
        ans = [set() for _ in range(n)]
        q = deque()
        for i in range(n):
            if ind[i] == 0:
                q += i,
        while q:
            u = q.popleft()
            for v in graph[u]:
                ind[v] -= 1
                ans[v].add(u)
                for ele in ans[u]:
                    ans[v].add(ele)
                if ind[v] == 0:
                    q += v,
        return [sorted(ele) for ele in ans]
