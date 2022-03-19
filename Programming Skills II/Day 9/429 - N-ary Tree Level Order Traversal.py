"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:  # 19.16% 94.82%
        if not root:
            return []
        stack = [root]
        out = [[root.val], []]
        while stack:
            next_row = []
            for node in stack:
                next_row.extend(node.children)
                out[-1].extend([x.val for x in node.children])
            stack = next_row
            out.append([])
        out.pop()
        out.pop()
        return out
                