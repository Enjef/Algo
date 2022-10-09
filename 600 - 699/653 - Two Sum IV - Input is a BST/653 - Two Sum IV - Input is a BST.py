# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:  # 30.34% 95.74%
        diff = set()
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            if k - node.val in diff:
                return True
            diff.add(node.val)
            stack.extend([node.right, node.left])
        return False

    # 69.87% 7.70%
    def findTarget_daily(self, root: Optional[TreeNode], k: int) -> bool:
        if not root.left and not root.right:
            return False

        def dfs(node):
            if not root:
                return
            if node.left:
                yield from dfs(node.left)
            yield node
            if node.right:
                yield from dfs(node.right)

        def target_search(node, second):
            if not node:
                return False
            if node == second:
                return (
                    target_search(node.left, second) or
                    target_search(node.right, second)
                )
            if node.val + second.val == k:
                return True
            left = right = False
            if node.left and node.val + second.val > k:
                left = target_search(node.left, second)
            if node.right and node.val + second.val < k:
                right = target_search(node.right, second)
            return left or right

        for node in dfs(root):
            if target_search(root, node):
                return True
        return False

    def findTarget_rec(self, root: TreeNode, k: int) -> bool:  # 38.84% 37.37%
        diff = set()

        def dfs(node):
            if not node:
                return False
            if k - node.val in diff:
                return True
            diff.add(node.val)
            return dfs(node.left) or dfs(node.right)
        return dfs(root)

    def findTarget_best_speed(self, root: Optional[TreeNode], k: int) -> bool:
        deque = [root]
        s = set()
        while deque:
            node = deque.pop(0)
            if k-node.val in s:
                return True
            s.add(node.val)
            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)
        return False

    def findTarget_best_memory(self, root: Optional[TreeNode], k: int) -> bool:
        values = []
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if True:
                for i in values:
                    if i + node.val == k:
                        return True
                values.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return False
