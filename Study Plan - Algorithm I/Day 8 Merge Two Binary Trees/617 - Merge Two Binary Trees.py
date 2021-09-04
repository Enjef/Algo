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
