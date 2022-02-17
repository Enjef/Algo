# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root, target: int): # 61.21% 91.64%
        def dfs(node):
            if not node:
                return False
            if not node.left and not node.right and node.val == target:
                return True
            left = dfs(node.left)
            if left:
                node.left = None
            right = dfs(node.right)
            if right:
                node.right = None
            if not node.left and not node.right and node.val == target:
                return True
            return False
            
        res = dfs(root)
        return None if res else root

    def removeLeafNodes_best_speed(self, root, target: int):
        def dfs(root):
            if not root: return None
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            if root.left == None and root.right == None and root.val == target:
                return None
            return root
        return dfs(root)

    def removeLeafNodes_2nd_best_speed_best_memory(self, root, target: int):
        if not root:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if not root.left and not root.right and root.val == target:
            return None
        return root
