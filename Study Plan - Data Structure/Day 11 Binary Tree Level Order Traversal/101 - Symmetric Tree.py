    def isSymmetric_sp_v2(
            self,
            root: Optional[TreeNode]) -> bool:  # 13.56% 93.33%
        stack_left = [root.left]
        stack_right = [root.right]
        while stack_left and stack_right:
            left = stack_left.pop()
            right = stack_right.pop()
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            stack_left.extend([left.left, left.right])
            stack_right.extend([right.right, right.left])
        if stack_left or stack_right:
            return False
        return True
