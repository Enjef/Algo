# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(
            self,
            root: Optional[TreeNode]) -> List[int]:  # 42.55% 80.54%
        if not root:
            return root
        out = [root.val]
        stack = [root]
        while stack:
            temp = []
            while stack:
                cur = stack.pop(0)
                if cur.left:
                    temp.append(cur.left)
                if cur.right:
                    temp.append(cur.right)
            if temp:
                out.append(temp[-1].val)
            stack = temp
        return out
