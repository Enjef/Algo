# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:  # 87.91% 97.75%
        arr = self.helper(root, [])
        first = arr[0]
        for i in range(1, len(arr)):
            arr[i-1].right = arr[i]
        return first

    def helper(self, root, array):
        if root.left:
            self.helper(root.left, array)
        root.left = None
        array.append(root)
        if root.right:
            self.helper(root.right, array)
        return array

    def increasingBST_daily(self, root: TreeNode) -> TreeNode:  # 91.17% 90.59%
        def dfs(node):
            nonlocal cur
            if node:
                dfs(node.left)
                cur.right = TreeNode(node.val)
                cur = cur.right
                dfs(node.right)
            return

        cur = dummy = TreeNode()
        dfs(root)
        return dummy.right

    def increasingBST_best(self, root: TreeNode) -> TreeNode:
        s = []
        tree = TreeNode(99)
        t = tree
        while True:
            if root:
                s.append(root)
                root = root.left
            elif s:
                root = s.pop()
                t.right = TreeNode(root.val)
                t = t.right
                root = root.right
            else:
                break
        return tree.right
