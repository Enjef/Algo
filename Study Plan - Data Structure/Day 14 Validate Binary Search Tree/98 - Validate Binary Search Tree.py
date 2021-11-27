class Solution:
    def isValidBST_ds_day_14(
            self,
            root: Optional[TreeNode]) -> bool:  # 24.08% 54.01%
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            cur, left, right = stack.pop()
            if not cur:
                continue
            if not(left<cur.val<right):
                return False
            stack.extend(
                [(cur.right, cur.val, right), (cur.left, left, cur.val)]
            )
        return True
