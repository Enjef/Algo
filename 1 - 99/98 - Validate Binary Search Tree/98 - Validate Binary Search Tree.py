class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:  # 91.81% 53.80%
        left = float('-inf')
        right = float('inf')
        stack = [(root, left, right)]
        while stack:
            cur, left, right = stack.pop()
            if not cur:
                continue
            if not(left < cur.val < right):
                return False
            stack.extend(
                [(cur.left, left, cur.val), (cur.right, cur.val, right)]
            )
        return True
