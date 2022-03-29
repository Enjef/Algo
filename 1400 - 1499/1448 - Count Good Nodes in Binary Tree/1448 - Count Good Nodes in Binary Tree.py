# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:  # 65.79%  86.79%
        def dfs_post(node, cur_max):
            nonlocal out
            if not node:
                return
            dfs_post(node.left, max(cur_max, node.val))
            dfs_post(node.right, max(cur_max, node.val))
            if node.val >= cur_max:
                out += 1
            return
            
        out = 0
        dfs_post(root, -10001)
        return out

    def goodNodes_best_speed(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if node.val >= max_val:
                max_val = node.val
                self.res += 1
            if node.left:
                dfs(node.left,max_val)
            if node.right:
                dfs(node.right,max_val)
        
        self.res = 0
        dfs(root, -inf)
        return self.res

    def goodNodes_best_memory(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.counter = 1
        
        def dfs(node):
            if not node:
                return
            if node.left:
                if node.left.val >= node.val:
                    self.counter += 1
                else:
                    node.left.val = node.val
            if node.right:
                if node.right.val >= node.val:
                    self.counter += 1
                else:
                    node.right.val = node.val
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.counter


class Solution_2nd_best_memory:
    def __init__(self):
        self.count = 0

    def goodNodes(self, root):
        for child in filter(None, [root.left, root.right]):
            self.count += child.val >= root.val
            child.val = max(child.val, root.val)
            self.goodNodes(child)
  
        return self.count + 1
