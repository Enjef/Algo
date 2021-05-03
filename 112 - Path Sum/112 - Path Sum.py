# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        summ = 0
        return self.summ_get(root, summ, targetSum)

    def summ_get(self, root, summ, targetSum):
        if not root:
            return False
        summ += root.val
        if not root.left and not root.right:
            if summ == targetSum:
                return True
        return (self.summ_get(root.left, summ, targetSum) or
                self.summ_get(root.right, summ, targetSum)
                )
