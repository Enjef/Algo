# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
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
