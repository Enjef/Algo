# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root):  # 75.76% 97.31%
        def helper(node):
            if not node:
                return
            helper(node.right)
            self.total += node.val
            node.val = self.total
            helper(node.left)
            return

        self.total = 0
        helper(root)
        return root

    def convertBST_best_speed(self, root):
        total = 0

        def traverse(root):
            nonlocal total
            if not root:
                return
            traverse(root.right)
            total += root.val
            root.val = total
            traverse(root.left)

        traverse(root)
        return root

    def convertBST_2nd_best_speed(self, root):
        self.curr_sum = 0

        def dfs(node):
            if node:
                dfs(node.right)
                node.val = node.val + self.curr_sum
                self.curr_sum = node.val
                dfs(node.left)

        dfs(root)
        return root

    def convertBST_4th_best_speed_bfs(self, root):
        acc, cur, stack = 0, root, []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                acc += cur.val
                cur.val = acc
                cur = cur.left
        return root
