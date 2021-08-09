# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:  # 95.66% 77.64%
        stack = [root]
        target = root.val
        while stack:
            cur = stack.pop()
            if cur.val != target:
                return False
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return True

    def isUnivalTree_best(self, root: TreeNode) -> bool:
        val = root.val
        def isvalid(root, val):
            if not root:
                return True
            if root.val != val:
                return False
            return isvalid(root.left, val) and isvalid(root.right, val)
        return isvalid(root, val)
