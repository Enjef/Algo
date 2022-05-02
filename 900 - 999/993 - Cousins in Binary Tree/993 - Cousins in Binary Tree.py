class Solution:
    def isCousins(
            self,
            root: Optional[TreeNode],
            x: int, y: int) -> bool:  # 31.85% 12.60%

        def dfs(node, depth, parent):
            nonlocal first, second
            if not node:
                return
            depth += 1
            if node.val == x:
                first = (parent, depth)
            if node.val == y:
                second = (parent, depth)
            dfs(node.left, depth, node)
            dfs(node.right, depth, node)

        first = second = None
        dfs(root, 0, None)
        return first[0] != second[0] and first[1] == second[1]

    def isCousins_v2(
            self,
            root: Optional[TreeNode], x: int, y: int) -> bool:  # 93.06% 49.40%
        stack = [(root, None)]
        out = []
        while stack:
            new_row = []
            for node, parent in stack:
                if node.val in (x, y):
                    out.append(parent)
                if node.left:
                    new_row.append((node.left, node))
                if node.right:
                    new_row.append((node.right, node))
            if out:
                return out[0] != out[-1]
            stack = new_row
        return

    def isCousins_best_speed(self, root, x, y):
        self.depthX = 0
        self.depthY = 0
        self.sameParent = False
        self.dfs(root, x, y, 0)
        return not self.sameParent and self.depthX == self.depthY

    def dfs(self, node, x, y, cur):
        if not node:
            return
        if node.val == x:
            self.depthX = cur
        if node.val == y:
            self.depthY = cur
        if node.left and node.right:
            left = node.left.val
            right = node.right.val
            if (left == x and right == y) or (left == y and right == x):
                self.sameParent = True
        self.dfs(node.left, x, y, cur+1)
        self.dfs(node.right, x, y, cur+1)

    def isCousins_2nd_best_speed(
            self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(T: TreeNode, par: TreeNode, dep, mp: dict):
            if not T:
                return
            if T.val in [x, y]:
                mp[T.val] = [par, dep]
            dfs(T.left, T, dep + 1, mp)
            dfs(T.right, T, dep + 1, mp)

        mp = {}
        dfs(root, None, 0, mp)
        if mp[x][1] == mp[y][1] and mp[x][0] != mp[y][0]:
            return True
        return False
