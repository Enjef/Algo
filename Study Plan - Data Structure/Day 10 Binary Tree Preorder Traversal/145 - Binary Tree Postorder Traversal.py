# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.out = []

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return self.out
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.out.append(root.val)
        return self.out
