# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root):  # 50.60% 5.65%
        def dfs(node, level):
            nonlocal level_max
            nonlocal deepest_leaves
            if not node.left and not node.right:
                if level > level_max:
                    deepest_leaves = set()
                    level_max = level
                if level == level_max:
                    deepest_leaves.add(node)
            if node.left:
                node.left.parent = node
                dfs(node.left, level+1)
            if node.right:
                node.right.parent = node
                dfs(node.right, level+1)
            return
        deepest_leaves = set()
        level_max = 0
        dfs(root, 0)
        while len(deepest_leaves) > 1:
            temp = set()
            for node in deepest_leaves:
                temp.add(node.parent)
            deepest_leaves = temp
        return deepest_leaves.pop()

    def lcaDeepestLeaves_best_speed(self, root):
        def dfs(node):
            if not node:
                return 0, None
            r_depth, r_lca = dfs(node.right)
            l_depth, l_lca = dfs(node.left)
            if r_depth > l_depth:
                return r_depth + 1, r_lca
            if l_depth > r_depth:
                return l_depth + 1, l_lca
            return l_depth + 1, node

        _, lca = dfs(root)
        return lca
