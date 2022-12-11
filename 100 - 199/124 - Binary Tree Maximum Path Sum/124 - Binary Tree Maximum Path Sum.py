# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 83.06% 20.23% (65.76% 10.62%)
    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return float('-inf')
            left = dfs(node.left)
            right = dfs(node.right)
            self.result = max(
                self.result,
                node.val,
                node.val+left,
                node.val+right,
                node.val+left+right
            )
            node.val = max(left+node.val, right+node.val, node.val)
            return node.val

        self.result = float('-inf')
        dfs(root)
        return self.result


class Solution_best_speed:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = [float('-inf')]

        def helper(root, maxsum):
            if not root:
                return 0
            left = helper(root.left, maxsum)
            right = helper(root.right, maxsum)
            temp = max(root.val, root.val+left, root.val+right)
            maxsum[0] = max(temp, root.val+left+right, maxsum[0])
            return temp

        helper(root, maxsum)
        return maxsum[0]


class Solution_best_memory:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        stack, node, last = [], root, None
        max_sum = None
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack[-1]
            if not node.right or node.right == last:
                node = stack.pop()
                max_child = 0
                max_val = 0
                if node.left and node.left.val > 0:
                    max_val += node.left.val
                    max_child = node.left.val
                if node.right and node.right.val > 0:
                    max_val += node.right.val
                    if max_child < node.right.val:
                        max_child = node.right.val
                if max_sum is None or node.val + max_val > max_sum:
                    max_sum = node.val + max_val
                node.val += max_child
                last = node
                node = None
            else:
                node = node.right
        return max_sum
