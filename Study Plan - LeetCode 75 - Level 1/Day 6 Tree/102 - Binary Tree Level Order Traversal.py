# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 88.38% 25.68%
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        stack = [root]
        out = []
        while stack:
            new = []
            out.append([])
            for node in stack:
                if not node:
                    continue
                out[-1].append(node.val)
                new.extend([node.left, node.right])
            stack = new
        out.pop()
        return out

    # 96.30% 83.92%
    def levelOrder_v2(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        stack = [root]
        out = []
        while stack:
            new = []
            out.append([])
            for node in stack:
                out[-1].append(node.val)
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            stack = new
        return out
