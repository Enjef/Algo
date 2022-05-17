# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:  # 37.00% 99.82%
        result = 0
        stack = [(root, root.val, root.val)]
        while stack:
            new = []
            for node, cur_min, cur_max in stack:
                if not node:
                    continue
                result = max(result, node.val-cur_min, cur_max-node.val)
                new.extend(
                    [(node.left, min(cur_min, node.val), max(cur_max, node.val)),
                     (node.right, min(cur_min, node.val), max(cur_max, node.val))])
            stack = new
        return result

    def maxAncestorDiff_best_speed(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, root.val, root.val)

    def helper(self, node, cur_min, cur_max):
        if not node:
            return cur_max - cur_min
        cur_max = max(cur_max, node.val)
        cur_min = min(cur_min, node.val)
        left = self.helper(node.left, cur_min, cur_max)
        right = self.helper(node.right, cur_min, cur_max)
        return max(left, right)

    def maxAncestorDiff_best_memory(self, root):
        if not root:
            return 0
        result = -1
        stack = [(root, root.val, root.val)]
        while stack:
            curr, vmax, vmin = stack.pop()
            vmax = max(curr.val, vmax)
            vmin = min(curr.val, vmin)
            result = max(vmax - vmin, result)
            if curr.left:
                stack.append((curr.left, vmax, vmin))
            if curr.right:
                stack.append((curr.right, vmax, vmin))
        return result
