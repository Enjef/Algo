# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):  # 78.99% 90.48%
        self.out = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.out.append(root.val)
            dfs(root.right)
            return
        dfs(root)

    def next(self) -> int:
        if self.out:
            return self.out.pop(0)

    def hasNext(self) -> bool:
        return bool(self.out)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

class BSTIterator_best_speed:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.stackWithLeft(root)

    def stackWithLeft(self, n):
        cur = n
        while cur:
            self.stack.append(cur)
            cur = cur.left
        
    def next(self) -> int:
        n = self.stack.pop()
        self.stackWithLeft(n.right)
        return n.val

    def hasNext(self) -> bool:
        return True if self.stack else False
