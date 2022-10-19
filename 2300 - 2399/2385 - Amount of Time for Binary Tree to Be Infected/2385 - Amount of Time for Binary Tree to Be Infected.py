# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 6.78% 91.37% (82.92% 91.37%)
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        stack = [root]
        while stack:
            new = []
            for node in stack:
                if node.left:
                    graph[node.val].append(node.left.val)
                    graph[node.left.val].append(node.val)
                    new.append(node.left)
                if node.right:
                    graph[node.val].append(node.right.val)
                    graph[node.right.val].append(node.val)
                    new.append(node.right)
            stack = new
        seen = {start}
        stack = [start]
        res = -1
        while stack:
            new = set()
            for node in stack:
                seen.add(node)
                new.update(graph[node])
            stack = new
            stack -= seen
            res += 1
        return res


class Solution_best_speed:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def dfs(node):
            if not node:
                return None
            if node.val == start:
                return [node]
            p = dfs(node.left)
            if p:
                p.append(node)
                return p
            p = dfs(node.right)
            if p:
                p.append(node)
                return p
            return None

        def depth(node, visited):
            if not node or node in visited:
                return 0
            q = [node]
            k = 0
            while q:
                nxt = []
                for i in q:
                    if i.left and i.left not in visited:
                        nxt.append(i.left)
                    if i.right and i.right not in visited:
                        nxt.append(i.right)
                if nxt:
                    k += 1
                q = nxt
            return k

        path = dfs(root)
        res = 0
        visited = set()
        for i in range(len(path)):
            res = max(res, depth(path[i], visited) + i)
            visited.add(path[i])
        return res


class Solution_4th_best_speed:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.ans = 0
        self.start = start
        self.root = root.val
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if not node:
            return 0, False
        left, left_bool = self.dfs(node.left)
        right, right_bool = self.dfs(node.right)
        if node.val == self.start:
            self.ans = max(self.ans, left, right)
            return 1, True
        if left_bool or right_bool:
            self.ans = max(self.ans, left + right)
        if left_bool:
            return left + 1, True
        if right_bool:
            return right + 1, True
        return max(left, right) + 1, False


class Solution_best_memory:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        stack = [(root, None)]
        while stack:
            n, p = stack.pop()
            if p:
                graph[p.val].append(n.val)
                graph[n.val].append(p.val)
            if n.left:
                stack.append((n.left, n))
            if n.right:
                stack.append((n.right, n))
        ans = -1
        seen = {start}
        queue = deque([start])
        while queue:
            for _ in range(len(queue)):
                u = queue.popleft()
                for v in graph[u]:
                    if v not in seen:
                        seen.add(v)
                        queue.append(v)
            ans += 1
        return ans
