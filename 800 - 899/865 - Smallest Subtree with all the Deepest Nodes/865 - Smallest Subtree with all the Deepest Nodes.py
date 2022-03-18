# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:  # 78.16% 6.22%
    def __init__(self):
        self.lvl = 0
        self.deepest = set()
    
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node, parent, cur_lvl):
            if cur_lvl == self.lvl:
                self.deepest.add(node)
            if cur_lvl > self.lvl:
                self.lvl = cur_lvl
                self.deepest = set([node])
            if node.left:
                dfs(node.left, node, cur_lvl+1)
            if node.right:
                dfs(node.right, node, cur_lvl+1)
            node.parent = parent
            return

        dfs(root, None, 0)
        while len(self.deepest) > 1:
            next_level = set()
            for node in self.deepest:
                next_level.add(node.parent)
            self.deepest = next_level
        return self.deepest.pop()


class Solution_best_speed:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if root.right == None and root.left == None:
            return root
        return self.dfs(root)[1]
    
    def dfs(self, node):
        if node == None:
            return (-1, None)
        l_height, left_node = self.dfs(node.left)
        r_height, right_node = self.dfs(node.right)
        if l_height == r_height:
            return (l_height + 1, node)
        elif l_height > r_height:
            return (l_height + 1, left_node)
        else:
            return (r_height + 1, right_node)
