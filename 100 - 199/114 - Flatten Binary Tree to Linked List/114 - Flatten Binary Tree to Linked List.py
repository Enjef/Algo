# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None: # 44.57% 94.65%
        arr = []
        def dfs(node):
            if not node:
                return
            arr.append(node)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            return
        dfs(root)
        if not arr:
            return []
        root = arr[0]
        for node in arr[1:]:
            root.left = None
            root.right = node
            root = root.right
        return arr[0]

class Solution_best_speed:
    def flatten(self, root: Optional[TreeNode]) -> None:
        return self.dfs(root)
        
    def dfs(self, node):
        if not node:
            return None
        L = self.dfs(node.left)
        R = self.dfs(node.right)
        if node.left:
            L.right= node.right
            node.right = node.left
            node.left= None
        last = R or L or node
        return last

class Solution_best_memory:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def visit(node):
            return [node] + visit(node.left) + visit(node.right) if node else []
        
        lst = visit(root)
        centinel = TreeNode()
        prev = centinel
        for node in lst:
            prev.right = node
            node.left = None
            prev = node
        prev.right = None
        return centinel.right
