# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(
            self,
            root: Optional[TreeNode]) -> List[List[int]]:  # 24.43% 45.03%
        if not root:
            return None
        stack = [root]
        out = []
        left = True
        while stack:
            temp = []
            level = []
            while stack:
                cur = stack.pop(0)
                level.append(cur.val)
                if cur.left:
                    temp.append(cur.left)
                if cur.right:
                    temp.append(cur.right)
            if left:
                out.append(level)
                left = False
            else:
                out.append(level[::-1])
                left = True
            stack = temp
        return out
