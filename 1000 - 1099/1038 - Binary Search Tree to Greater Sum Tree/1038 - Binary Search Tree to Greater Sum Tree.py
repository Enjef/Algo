# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst_my(self, root: TreeNode) -> TreeNode:  # 99.63%
        stack = [root]
        v_map = []
        while stack:
            cur = stack.pop()
            v_map.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        v_map.sort()
        stack = [root]
        while stack:
            cur = stack.pop()
            cur.val = sum(v_map[v_map.index(cur.val):])
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return root

    def bstToGst_best(self, root: TreeNode) -> TreeNode:
        self.total = 0

        def recurse(node):
            if node is None:
                return
            recurse(node.right)
            self.total += node.val
            node.val = self.total
            recurse(node.left)
        recurse(root)
        return root
