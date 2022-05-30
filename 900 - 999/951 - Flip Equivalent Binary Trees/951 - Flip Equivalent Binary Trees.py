# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(
            self, root1: Optional[TreeNode],
            root2: Optional[TreeNode]) -> bool:  # 55.93% 32.83%

        def dfs(node, way):
            if not node:
                way.append(None)
                return way
            if node.left and node.right:
                if node.left.val > node.right.val:
                    node.left, node.right = node.right, node.left
            if not node.left and node.right:
                node.left, node.right = node.right, None
            way.append(node.val)
            dfs(node.left, way)
            dfs(node.right, way)
            return way

        first = dfs(root1, [])
        second = dfs(root2, [])
        return first == second

    def flipEquiv_best_speed(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        return ((self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right))
                or (self.flipEquiv(root1.right, root2.left) and self.flipEquiv(root1.left, root2.right)))

    def flipEquiv_2nd_best_speed(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None and root2:
            return False
        if root2 is None and root1:
            return False
        if root1 and root2 and root1.val != root2.val:
            return False
        if root1 is root2:
            return True
        return (
            self.flipEquiv(root1.left, root2.left) and
            self.flipEquiv(root1.right, root2.right) or
            self.flipEquiv(root1.right, root2.left) and
            self.flipEquiv(root1.left, root2.right)
        )

    def flipEquiv_best_memory(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def helper(root1, root2):
            if not root1 and not root2:
                return True
            elif not root1 or not root2 or root1.val != root2.val:
                return False
            else:
                return (
                    helper(root1.left, root2.left) and
                    helper(root1.right, root2.right)) or (
                        helper(root1.left, root2.right) and
                        helper(root1.right, root2.left))

        return helper(root1, root2)
