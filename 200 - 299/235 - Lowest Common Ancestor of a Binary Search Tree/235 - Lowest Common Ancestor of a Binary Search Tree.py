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

    def lowestCommonAncestor_best_speed(
            self,
            root: 'TreeNode',
            p: 'TreeNode',
            q: 'TreeNode') -> 'TreeNode':
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root

    def lowestCommonAncestor_4th_best_speed_stack(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_val = p.val
        q_val = q.val
        node = root
        while node:
            parent_val = node.val
            if p_val > parent_val and q_val > parent_val:    
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                node = node.left
            else:
                return node
