# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:  # 79.19% 56.21%
        level = 1
        stack = [root]
        max_sum = [root.val, level]
        while stack:
            next_row = []
            cur_sum = 0
            for node in stack:
                cur_sum += node.val
                if node.left:
                    next_row.append(node.left)
                if node.right:
                    next_row.append(node.right)
            stack = next_row
            if cur_sum > max_sum[0]:
                max_sum = [cur_sum, level]
            level += 1
        return max_sum[1]
