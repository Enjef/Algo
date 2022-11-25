class Solution:
    # 17.20% 23.58% (10.29% 23.41%)
    def longestPath(self, parent: List[int], s: str) -> int:
        class Node:
            def __init__(self, val, children):
                self.val = val
                self.children = children

        def dfs(node):
            if not node.children:
                return 1
            go = []
            for child in node.children:
                x = dfs(child)
                if child.val != node.val:
                    go.append(x)
                else:
                    go.append(0)
            first = second = 0
            go.sort()
            if go:
                first = go.pop()
            if go:
                second = go.pop()
            self.longest = max(self.longest, first + second + 1)
            return max(first, second) + 1

        n = len(parent)
        new = [Node(char, []) for char in s]
        for i in range(1, n):
            new[parent[i]].children.append(new[i])

        self.longest = 1
        dfs(new[0])
        return self.longest


class Solution_best_speed:
    def longestPath(self, parents: List[int], s: str) -> int:
        def post_order(node):
            kid1, kid2, ch = 0, 0, s[node]
            for kid in kids[node]:
                curr_kid = post_order(kid)
                if s[kid] != ch:
                    if kid1 < curr_kid:
                        kid1, kid2 = curr_kid, kid1
                    elif kid2 < curr_kid:
                        kid2 = curr_kid
            curr_path = 1 + kid1 + kid2
            if self.longest < curr_path:
                self.longest = curr_path
            return 1 + kid1

        kids, self.longest = [[] for _ in range(len(parents))], 0
        for kid, parent in enumerate(parents[1:], 1):
            kids[parent].append(kid)
        post_order(0)
        return self.longest

    def longestPath_2nd(self, parent: List[int], s: str) -> int:
        dic = collections.defaultdict(list)
        self.ret = 1
        for ind, val in enumerate(parent):
            if val < 0:
                continue
            dic[val].append(ind)

        def dfs(ind, dic, s):
            if ind not in dic:
                return 1
            m1 = 0
            m2 = 0
            for item in dic[ind]:
                if s[item] == s[ind]:
                    dfs(item, dic, s)
                else:
                    temp = dfs(item, dic, s)
                    if m1 == m2 and m2 == 0:
                        m1 = temp
                    elif temp >= m1:
                        m2 = m1
                        m1 = temp
                    elif temp < m1 and temp > m2:
                        m2 = temp
            self.ret = max(self.ret, m1+m2+1)
            return m1+1

        dfs(0, dic, s)
        return self.ret

    max_len = 1
    children = []

    def longestPath_3d(self, parent: List[int], s: str) -> int:
        self.children = defaultdict(list)
        for i in range(len(parent)):
            self.children[parent[i]].append(i)
        self.dfs(0, s)
        return self.max_len

    def dfs(self, node, s):
        if not self.children[node]:
            return 1
        first_path, second_path = 0, 0
        for child in self.children[node]:
            path_len = self.dfs(child, s)
            if s[node] != s[child]:
                if path_len > first_path:
                    second_path = first_path
                    first_path = path_len
                elif path_len > second_path:
                    second_path = path_len
                if first_path + second_path + 1 > self.max_len:
                    self.max_len = first_path + second_path + 1
        return first_path + 1


class Solution_best_memory:
    def longestPath(self, parent: List[int], s: str) -> int:
        cnt = [0] * len(parent)
        top1 = [1] * len(parent)
        top2 = [1] * len(parent)
        for i in range(1, len(parent)):
            cnt[parent[i]] += 1
        queue = collections.deque([])
        for i in range(1, len(parent)):
            if cnt[i] == 0:
                queue.append(i)
        ans = 1
        while queue:
            curr = queue.popleft()
            curr_parent = parent[curr]
            if curr_parent == -1:
                break
            if s[curr_parent] != s[curr]:
                arrow = top1[curr] + 1
                if arrow >= top1[curr_parent]:
                    top2[curr_parent] = top1[curr_parent]
                    top1[curr_parent] = arrow
                else:
                    top2[curr_parent] = max(top2[curr_parent], arrow)
            ans = max(ans, top1[curr_parent] + top2[curr_parent] - 1)
            cnt[curr_parent] -= 1
            if cnt[curr_parent] == 0:
                queue.append(curr_parent)
        return ans

    def longestPath_2nd(self, parent: List[int], s: str) -> int:
        n = len(s)
        indegree = [0]*n
        for i, p in enumerate(parent):
            if i != 0:
                indegree[p] += 1
        ans = 0
        queue = deque(i for i, d in enumerate(indegree) if d == 0)
        paths_to = [[] for _ in range(n)]
        while queue:
            node = queue.popleft()
            longest = 0
            if paths_to[node]:
                ans = max(ans, sum(paths_to[node]))
                longest = max(paths_to[node])
            p = parent[node]
            if s[p] != s[node]:
                heappush(paths_to[p], longest+1)
                if len(paths_to[p]) > 2:
                    heappop(paths_to[p])
            indegree[p] -= 1
            if indegree[p] == 0:
                queue.append(p)
        return ans + 1
