# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(
            self,
            root: Optional[TreeNode],
            targetSum: int) -> List[List[int]]:  # 53.46% 30.89%
        def dfs(root, cur, target, out):
            if not root.left and not root.right and target-root.val == 0:
                out.append(cur+[root.val])
            if root.left:
                dfs(root.left, cur+[root.val], target-root.val, out)
            if root.right:
                dfs(root.right, cur+[root.val], target-root.val, out)
            return out
        if not root:
            return root
        return dfs(root, [], targetSum, [])
