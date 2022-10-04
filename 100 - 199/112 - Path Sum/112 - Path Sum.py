# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:  # 99.76% 1%
        summ = 0
        return self.summ_get(root, summ, targetSum)

    def summ_get(self, root, summ, targetSum):
        if not root:
            return False
        summ += root.val
        if not root.left and not root.right:
            if summ == targetSum:
                return True
        return (
            self.summ_get(root.left, summ, targetSum) or
            self.summ_get(root.right, summ, targetSum)
        )

    def hasPathSum_ds_day_11(
            self,
            root: Optional[TreeNode], targetSum: int) -> bool:  # 84.49% 99.53%
        if not root:
            return False
        stack = [(root, 0)]
        while stack:
            node, cur = stack.pop()
            if not node.left and not node.right:
                if cur + node.val == targetSum:
                    return True
                continue
            if node.left:
                stack.append((node.left, cur+node.val))
            if node.right:
                stack.append((node.right, cur+node.val))
        return False


class Solution_v2:
    # 76.91% 91.98%
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum-root.val == 0
        return (
            self.hasPathSum(root.left, targetSum-root.val) or
            self.hasPathSum(root.right, targetSum-root.val))


class Solution_oneliner:
    # 14.63% 91.98%
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return not root.left and not root.right and (targetSum-root.val==0) or self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val) if root else False


class Solution_oneliner_v2:
    # 75.65% 91.98%
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return root and (root.left==root.right and targetSum==root.val or self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val))
