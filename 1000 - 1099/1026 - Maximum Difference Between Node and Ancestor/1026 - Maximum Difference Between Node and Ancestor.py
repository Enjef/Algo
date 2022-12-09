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


# 87.72% 7.79% (18.34%  6.31%)
class Solution_one_liner:
    def maxAncestorDiff(self, root: Optional[TreeNode], min_val=10**5+1, max_val=0) -> int:
        return 0 if not root else max(root.val-min_val, max_val-root.val, self.maxAncestorDiff(root.left, min(min_val, root.val), max(max_val, root.val)), self.maxAncestorDiff(root.right, min(min_val, root.val), max(max_val, root.val)))


# 53.37% 6.31% (40.05% 6.31%)
class Solution_one_liner_walrus:
    def maxAncestorDiff(self, root: Optional[TreeNode], min_val=10**5+1, max_val=0) -> int:
        return 0 if not root else max(root.val-min_val, max_val-root.val, self.maxAncestorDiff(root.left, min_val:=min(min_val, root.val), max_val:=max(max_val, root.val)), self.maxAncestorDiff(root.right, min_val, max_val))


class Solution_best_speed:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, root.val, root.val)

    def helper(self, node, cur_min, cur_max):
        if not node:
            return cur_max - cur_min
        cur_max = max(cur_max, node.val)
        cur_min = min(cur_min, node.val)
        left = self.helper(node.left, cur_min, cur_max)
        right = self.helper(node.right, cur_min, cur_max)
        return max(left, right)


class Solution_best_memory:
    def maxAncestorDiff(self, root):
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
