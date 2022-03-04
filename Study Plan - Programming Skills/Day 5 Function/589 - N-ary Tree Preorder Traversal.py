"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:  # 70.84% 29.82%
        def dfs(node):
            if not node:
                return
            out.append(node.val)
            for sub in node.children:
                dfs(sub)
            return
        
        out = []
        dfs(root)
        return out
