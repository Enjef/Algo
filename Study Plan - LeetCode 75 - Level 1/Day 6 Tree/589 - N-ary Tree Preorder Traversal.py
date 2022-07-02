"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    # 49.34% 14.59% (94.77% 14.59%)
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(node):
            if not node:
                return
            out.append(node.val)
            for child in node.children:
                dfs(child)
            return

        out = []
        dfs(root)
        return out
