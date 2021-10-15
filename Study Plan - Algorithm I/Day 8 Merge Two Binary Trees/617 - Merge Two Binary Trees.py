class Solution:
    def mergeTrees(
            self,
            root1: Optional[TreeNode],
            root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        stack = [[root1, root2]]
        while stack:
            cur_one, cur_two = stack.pop()
            cur_one.val += cur_two.val
            if cur_one.left and cur_two.left:
                stack.append([cur_one.left, cur_two.left])
            if cur_one.right and cur_two.right:
                stack.append([cur_one.right, cur_two.right])
            if not cur_one.left and cur_two.left:
                cur_one.left = cur_two.left
            if not cur_one.right and cur_two.right:
                cur_one.right = cur_two.right
        return root1

    def mergeTrees_rec(
            self,
            root1: Optional[TreeNode],
            root2: Optional[TreeNode]) -> Optional[TreeNode]:  # 64.24% 77.23%
        if root1 and root2:
            root = TreeNode(root1.val + root2.val)
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
            return root
        else:
            return root1 or root2
