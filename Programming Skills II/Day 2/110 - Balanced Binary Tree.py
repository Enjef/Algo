class Solution:
    def isBalanced1(self, root: Optional[TreeNode]) -> bool:  # 61.93% 59.31%
        if not root:
            return 1
        left = self.isBalanced1(root.left)
        right = self.isBalanced1(root.right)
        if abs(left-right) > 1:
            return float('inf')
        return max(left+1, right+1)
    
    def isBalanced(self, root):
        return self.isBalanced1(root) != float('inf')
