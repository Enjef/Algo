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