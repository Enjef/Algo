# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root, low, high):  # 60.80% 83.03%
        def search_valid(target):
            if low <= target.val <= high:
                return target
            left = search_valid(target.left) if target.left else None
            right = search_valid(target.right) if target.right else None
            return left or right

        def dfs(node):
            if not node:
                return
            if node.left and not(low <= node.left.val <= high):
                node.left = search_valid(node.left)
            if node.right and not(low <= node.right.val <= high):
                node.right = search_valid(node.right)
            dfs(node.left)
            dfs(node.right)
            return

        if not(low <= root.val <= high):
            root = search_valid(root)
        dfs(root)
        return root

    def trimBST_v2(self, root, low, high):  # 79.50% 11.70%
        def search_valid(target):
            if low <= target.val <= high:
                return target
            left = search_valid(target.left) if target.left else None
            right = search_valid(target.right) if target.right else None
            return left or right

        def dfs(node):
            if not node:
                return
            if node.left and not(low <= node.left.val):
                node.left = search_valid(node.left)
            if node.right and not(node.right.val <= high):
                node.right = search_valid(node.right)
            dfs(node.left)
            dfs(node.right)
            return

        if not(low <= root.val <= high):
            root = search_valid(root)
        dfs(root)
        return root


class Solution_best_speed:
    def recur(self, node, low, high):
        if node is None:
            return
        if node.left and node.left.val < low:
            node.left = node.left.right
            self.recur(node, low, high)
        self.recur(node.left, low, high)
        if node.right and node.right.val > high:
            node.right = node.right.left
            self.recur(node, low, high)
        self.recur(node.right, low, high)

    def trimBST(self, root, low, high):
        while root and (root.val < low or root.val > high):
            if root.val < low:
                root = root.right
            elif root.val > high:
                root = root.left
        self.recur(root, low, high)
        return root


class Solution_2nd_best_speed:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int):
        if root is None:
            return
        if root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            return self.trimBST(root.left, low, high)
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root


class Solution_best_memory:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int):
        if not root:
            return None
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root if low <= root.val <= high else root.left or root.right


class Solution_2nd_best_memory:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int):
        def trim(root, low, high):
            if root is None:
                return None
            root.left = trim(root.left, low, high)
            root.right = trim(root.right, low, high)
            if root.val < low:
                return root.right
            if root.val > high:
                return root.left
            return root
        return trim(root, low, high)
