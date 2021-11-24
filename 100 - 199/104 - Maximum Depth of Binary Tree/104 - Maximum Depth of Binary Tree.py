# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:  # 92.58%  40.89%
        count = 0
        return self.count_depth(root, count)

    def count_depth(self, root, count):
        if root:
            count += 1
            return max(
                self.count_depth(root.right, count),
                count,
                self.count_depth(root.left, count)
            )
        return count

    def maxDepth_sp_stack(
            self,
            root: Optional[TreeNode]) -> int:  # 22.40% 96.02%
        if not root:
            return 0
        stack = [(root, 1)]
        max_level = 1
        while stack:
            node, level = stack.pop()
            max_level = max(max_level, level)
            if node.left:
                stack.append((node.left, level+1))
            if node.right:
                stack.append((node.right, level+1))
        return max_level

    def maxDepth_sp_rec(
            self,
            root: Optional[TreeNode]) -> int:  # 52.54% 18.65%
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth_best_speed(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root and not root.left and not root.right:
            return 1
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)

    def maxDepth_2nd_best_memory(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = [root]
        res = 0
        while q:
            tq = []
            for n in q:
                if n.left:
                    tq.append(n.left)
                if n.right:
                    tq.append(n.right)
            q = tq
            res += 1
        return res
