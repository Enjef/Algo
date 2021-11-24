class Solution:
    def maxDepth_stack(self, root: Optional[TreeNode]) -> int:  # 22.40% 96.02%
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

    def maxDepth_rec(self, root: Optional[TreeNode]) -> int:  # 52.54% 18.65%
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
