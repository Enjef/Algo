# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.out = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return self.out
        self.inorderTraversal(root.left)
        self.out.append(root.val)
        return self.inorderTraversal(root.right)
