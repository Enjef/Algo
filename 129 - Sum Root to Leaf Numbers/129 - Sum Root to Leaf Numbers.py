# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers_first(self, root: TreeNode) -> int:  # Runtime: 40 ms, faster than 5.08%, Memory Usage: 14.3 MB, less than 48.86%
        out = 0
        curr = ''
        def helper(root, curr, out):
            curr += str(root.val)
            if not root.left and not root.right:
                out += int(curr)
                return out
            if root.left and root.right:
                return helper(root.left, curr, out) + helper(root.right, curr, out)
            if root.left:
                return helper(root.left, curr, out)
            if root.right:
                return helper(root.right, curr, out)
        return helper(root, curr, out)

    def sumNumbers_second(self, root: TreeNode) -> int: #  Runtime: 32 ms, faster than 57.88%, Memory Usage: 14.4 MB, less than 16.33% 
        self.out = 0
        def helper(root, curr):
            if not root:
                return
            curr += str(root.val)
            if not root.left and not root.right:
                self.out += int(curr)
            helper(root.left, curr)
            helper(root.right, curr)
        helper(root, '')
        return self.out
