# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(
            self,
            root: 'TreeNode',
            p: 'TreeNode',
            q: 'TreeNode') -> 'TreeNode':  # 28.83% 78.78%
        if min(p.val, q.val) <= root.val <= max(p.val, q.val):
            return root
        if root.val in [p.val, q.val]:
            return p if p.val < q.val else q
        if p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
