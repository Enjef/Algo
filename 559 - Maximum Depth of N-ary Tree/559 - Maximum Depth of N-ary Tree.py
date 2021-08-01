"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:  # 98.45% 80.98%
        if not root:
            return 0
        if not root.children:
            return 1
        return max([self.maxDepth(child) for child in root.children]) + 1

    def maxDepth_best(self, root: 'Node') -> int:
        if not root:
            return 0
        depth = 0
        for child in root.children:
            child_depth = self.maxDepth(child)
            if child_depth > depth:
                depth = child_depth
        return depth + 1
