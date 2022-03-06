# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:  # 93.72% 93.18%
        if not root:
            return 0
        out = 0
        stack = [root]
        while stack:
            temp = []
            for el in stack:
                if not el:
                    continue
                temp.extend([el.left, el.right])
            stack = temp
            if temp:
                out += 1
        return out

    def maxDepth(self, root: Optional[TreeNode]) -> int:  # 60.68% 99.08%
        if not root:
            return 0
        out = 0
        stack = [root]
        while stack:
            temp = []
            for el in stack:
                if el.left:
                    temp.append(el.left)
                if el.right:
                    temp.append(el.right)
            stack = temp
            out += 1
        return out
