# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:  # 97.46% 94.49 %
        stack = [(root, False)]
        out_sum = 0
        while stack:
            root, left = stack.pop()
            if not root.left and not root.right and left:
                out_sum += root.val
            if root.left:
                stack.append((root.left, True))
            if root.right:
                stack.append((root.right, False))
        return out_sum

    def sumOfLeftLeaves_best_speed(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def traverse(node, pos):
            if not node:
                return
            if pos == 'left' and not node.left and not node.right:
                self.res += node.val
            traverse(node.left, 'left')
            traverse(node.right, 'right')
        
        traverse(root, '')
        return self.res
