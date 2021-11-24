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

    def isSymmetric_sp_v2(
            self,
            root: Optional[TreeNode]) -> bool:  # 13.56% 93.33%
        stack_left = [root.left]
        stack_right = [root.right]
        while stack_left and stack_right:
            left = stack_left.pop()
            right = stack_right.pop()
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            stack_left.extend([left.left, left.right])
            stack_right.extend([right.right, right.left])
        if stack_left or stack_right:
            return False
        return True
