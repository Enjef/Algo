# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return None
        out = []
        stack = [root]
        while stack:
            root = stack.pop()
            out.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return out[::-1]

    def postorderTraversal_ds_day_10(
            self,
            root: Optional[TreeNode]) -> List[int]:  # 22.68% 98.93%
        def dfs(root, out):
            if not root:
                return out
            dfs(root.left, out)
            dfs(root.right, out)
            out.append(root.val)
            return out
        return dfs(root, [])

    def postorderTraversal_best_speed(
            self,
            root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        def postorder(node):
            if node:
                postorder(node.left)
                postorder(node.right)
                res.append(node.val)
        postorder(root)

    def postorderTraversal_3d_best_speed(
            self,
            root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return (
            self.postorderTraversal(root.left) +
            self.postorderTraversal(root.right) +
            [root.val]
        )
