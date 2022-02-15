# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root): # 94.51% 91.16%
        def dfs(node):
            if not node:
                return False
            res = node.val == 1
            left = dfs(node.left)
            if not left:
                node.left = None
            right = dfs(node.right)
            if not right:
                node.right = None
            return res or left or right
        
        out = dfs(root)
        return root if out else None

    def pruneTree_best_memory(self, root):
        if not root:
            return root
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val == 0 and (not root.left) and (not root.right):
            return None
        else:
            return root
