class Solution:
    def insertIntoBST(
            self,
            root: Optional[TreeNode],
            val: int) -> Optional[TreeNode]:  # 25.79% 28.16%
        cur = root
        to_insert = TreeNode(val)
        if not cur:
            return to_insert
        while True:
            if cur.val > val:
                if not cur.left:
                    cur.left = to_insert
                    return root
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = to_insert
                    return root
                cur = cur.right
