# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        count = 0
        return self.count_depth(root, count)

    def count_depth(self, root, count):
        if root:
            count += 1
            return max(
                self.count_depth(root.right, count),
                count,
                self.count_depth(root.left, count)
            )
        return count
