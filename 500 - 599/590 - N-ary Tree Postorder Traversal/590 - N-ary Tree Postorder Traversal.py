"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder_stack(self, root: 'Node') -> List[int]:  # 61.30% 90.80%
        if not root:
            return root
        stack = [root]
        out = []
        while stack:
            cur = stack.pop()
            out.append(cur.val)
            stack.extend(cur.children)
        return out[::-1]

    def postorder_rec(self, root: 'Node') -> List[int]:  # 82.59% 90.80%
        if not root:
            return root
        out = []
        def helper(root1):
            for child in root1.children:
                helper(child)
            out.append(root1.val)
            return out
        return helper(root)
