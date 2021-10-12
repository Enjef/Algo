# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:  # 60.62% 78.13 %
        if not root:
            return True
        return self.compare(root.left, root.right)

    def compare(self, left, right):
        if left and right:
            return (
                left.val == right.val and
                self.compare(left.left, right.right) and
                self.compare(left.right, right.left)
            )
        return left == right

    def isSymmetric_stack(self, root):  # 60.62% 92.52%
        if not root:
            return True
        stack = [root.left, root.right]
        while stack:
            right = stack.pop()
            left = stack.pop()
            if not right and not left:
                continue
            if not right and left or not left and right:
                return False
            if right.val != left.val:
                return False
            stack += [left.left, right.right, left.right, right.left]
        return True
