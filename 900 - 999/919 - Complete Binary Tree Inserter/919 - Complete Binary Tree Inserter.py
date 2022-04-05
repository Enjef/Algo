# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:
    def __init__(self, root: Optional[TreeNode]):  # 9.77% 73.64%
        self.root = root

    def insert(self, val: int) -> int:
        stack = [self.root]
        while stack:
            next_row = []
            for node in stack:
                if not node:
                    continue
                if not node.left:
                    node.left = TreeNode(val=val)
                    return node.val
                if not node.right:
                    node.right = TreeNode(val=val)
                    return node.val
                next_row.extend([node.left, node.right])
            stack = next_row
        return

    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()


class CBTInserter_best_speed:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.leafs = collections.deque([])
        self.build_leafs(root)

    def build_leafs(self, node: Optional[TreeNode]):
        nodes = collections.deque([node])
        while nodes:
            node = nodes.popleft()
            if node.left and node.right:
                nodes.append(node.left)
                nodes.append(node.right)
            elif node.left or node.right:
                nodes.append(node.left or node.right)
                self.leafs.append(node)
            else:
                self.leafs.append(node)

    def insert(self, val: int) -> int:
        result = self.leafs[0].val
        node = TreeNode(val)
        if self.leafs[0].left:
            leaf = self.leafs.popleft()
            leaf.right = node
        else:
            self.leafs[0].left = node
        self.leafs.append(node)
        return result

    def get_root(self) -> Optional[TreeNode]:
        return self.root


class CBTInserter_2nd_best_speed:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.q = deque([])
        q = deque([root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.q.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, val: int) -> int:
        node = self.q[0]
        self.q.append(TreeNode(val))
        if not node.left:
            node.left = self.q[-1]
        else:
            node.right = self.q[-1]
            self.q.popleft()
        return node.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root


class CBTInserter_3rd_best_speed:
    def __init__(self, root: Optional[TreeNode]):
        self.list = [root]
        from collections import deque
        queue = deque([root])
        while queue:
            sz = len(queue)
            for i in range(sz):
                node = queue.pop()
                if node.left:
                    queue.appendleft(node.left)
                    self.list.append(node.left)
                if node.right:
                    queue.appendleft(node.right)
                    self.list.append(node.right)

    def insert(self, val: int) -> int:
        new = TreeNode(val)
        self.list.append(new)
        index = len(self.list)-1
        parent = (index-1) // 2
        res = (index-1) % 2
        if res == 0:
            self.list[parent].left = new
        else:
            self.list[parent].right = new
        return self.list[parent].val

    def get_root(self) -> Optional[TreeNode]:
        return self.list[0]


class CBTInserter_best_memory:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.dq = collections.deque([self.root])

    def insert(self, val: int) -> int:
        while self.dq[0].right:
            node = self.dq.popleft()
            self.dq.append(node.left)
            self.dq.append(node.right)
        parent = self.dq[0]
        if parent.left:
            parent.right = TreeNode(val)
        else:
            parent.left = TreeNode(val)
        return parent.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root
