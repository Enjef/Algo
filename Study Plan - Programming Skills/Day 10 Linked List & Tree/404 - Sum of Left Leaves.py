# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root):  # 56.83% 95.52%
        total = 0
        stack = [(root, False)]
        while stack:
            level = []
            for el, is_left in stack:
                if not el.left and not el.right and is_left:
                    total += el.val
                    continue
                if el.left:
                    level.append((el.left, True))
                if el.right:
                    level.append((el.right, False))
            stack = level
        return total
