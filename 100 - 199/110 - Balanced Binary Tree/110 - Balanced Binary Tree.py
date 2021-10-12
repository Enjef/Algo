# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def h_count(root):
            if not root:
                return 0
            left, right = h_count(root.left), h_count(root.right)
            if abs(left - right) > 1:
                return float('inf')
            return max(left, right) + 1
        return h_count(root) != float('inf')
