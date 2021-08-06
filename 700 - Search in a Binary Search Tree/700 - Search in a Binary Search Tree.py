# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:  # 50.72% 71.21%
        if not root:
            return root
        if root.val == val:
            return root
        return (
            self.searchBST(root.left, val) or self.searchBST(root.right, val)
        )

    def helper(self, node, val):
        if node is None:
            return None
        elif node.val == val:
            return node
        elif node.val > val:
            return self.helper(node.left, val)
        else:
            return self.helper(node.right, val)

    def searchBST_best(self, root: TreeNode, val: int) -> TreeNode:
        return self.helper(root, val)
