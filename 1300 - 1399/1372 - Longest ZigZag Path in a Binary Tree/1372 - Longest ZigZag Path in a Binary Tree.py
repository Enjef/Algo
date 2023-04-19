# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 51.65% 82.05% (69.96% 86.45%)
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node, prev):
            if not node:
                return 0
            cur = 0
            if prev != 'L':
                dfs(node.right, 'R')
                cur = dfs(node.left, 'L')
            elif prev != 'R':
                dfs(node.left, 'L')
                cur = dfs(node.right, 'R')
            self.res = max(self.res, cur+int(prev is not None))
            return cur + 1

        self.res = 0
        dfs(root, None)
        return self.res


class Solution_best_speed:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def recursive(node, lr, len_):
            result.append(len_)
            if node.left is None and node.right is None:
                return
            if lr == 'l':
                if node.left is not None:
                    recursive(node.left, 'l', 1)
                if node.right is not None:
                    recursive(node.right, 'r', len_ + 1)
            elif lr == 'r':
                if node.left is not None:
                    recursive(node.left, 'l', len_ + 1)
                if node.right is not None:
                    recursive(node.right, 'r', 1)

        result = []
        if root.left is not None:
            recursive(root.left, 'l', 1)
        if root.right is not None:
            recursive(root.right, 'r', 1)
        if len(result) != 0:
            return max(result)
        return 0


# 98.53% 99.27%
class Solution_5th_best_speed:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque([(root, 0, 0)])
        best = 0
        while queue:
            node, toLeft, toRight = queue.popleft()
            best = max(best, toLeft, toRight)
            if node.right:
                queue.append((node.right, 0, toLeft+1))
            if node.left:
                queue.append((node.left, toRight+1, 0))
        return best
