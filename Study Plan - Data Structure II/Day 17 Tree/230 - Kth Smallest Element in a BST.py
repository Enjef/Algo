# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(
            self,
            root: Optional[TreeNode],
            k: int) -> int:  # 63.70% 96.42%
        out = []
        stack = [root]
        while stack:
            cur = stack.pop()
            out.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        out.sort()
        return out[k-1]
