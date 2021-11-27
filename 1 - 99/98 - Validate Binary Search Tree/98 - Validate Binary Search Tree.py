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

    def isValidBST_best_speed(self, root: Optional[TreeNode]) -> bool:
        left = self.validTree(root.left, -sys.maxsize, root.val)
        right = self.validTree(root.right, root.val, sys.maxsize)
        return left and right

    def validTree(self, root, low, high):
        if not root:
            return True
        if root.val <= low or root.val >= high:
            return False
        left = self.validTree(root.left, low, root.val)
        right = self.validTree(root.right, root.val, high)
        return left and right

    def isValidBST_2d_best_speed(self, root: Optional[TreeNode]) -> bool:
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            if node.val <= lower or node.val >=upper :
                return False
            if not helper(node.right, node.val, upper):
                return False
            if not helper(node.left, lower,node.val):
                return False
            return True
        return helper(root)
