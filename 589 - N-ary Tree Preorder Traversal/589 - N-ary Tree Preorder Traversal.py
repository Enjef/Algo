"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:  # 60.83% 22.90%
        out = []
        if not root:
            return out
        stack = [root]
        while stack:
            cur = stack.pop()
            out.append(cur.val)
            stack.extend(cur.children[::-1])
        return out

    def preorder_best(self, root: 'Node') -> List[int]:  # best
        output = []

        def dfs(node):
            if not node:
                return
            output.append(node.val)
            for c in node.children:
                dfs(c)
        dfs(root)
        return output
