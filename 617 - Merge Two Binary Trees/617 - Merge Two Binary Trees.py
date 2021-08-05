# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(
            self,
            root1: TreeNode,
            root2: TreeNode) -> TreeNode:  # 78.12% 50.17%
        if not root1:
            return root2
        if not root2:
            return root1
        out = TreeNode(0, root1, None)
        def helper(root1, root2, parent, direction):
            if not root1 and not root2:
                return out.left
            if not root1 and root2:
                if direction == 'left':
                    parent.left = root2
                else:
                    parent.right = root2
                return out.left
            if root1 and root2:
                root1.val += root2.val
                helper(root1.left, root2.left, root1, 'left')
                helper(root1.right, root2.right, root1, 'right')
            return out.left
        helper(root1, root2, out, None)
        return out.left

    def mergeTrees_best(
            self,
            root1: TreeNode,
            root2: TreeNode) -> TreeNode:
        if root1 is None:
            return root2

        if root2 is None:
            return root1

        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1
