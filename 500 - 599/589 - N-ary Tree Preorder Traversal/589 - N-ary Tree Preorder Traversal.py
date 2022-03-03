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

    def preorder_best(self, root: 'Node') -> List[int]:
        output = []

        def dfs(node):
            if not node:
                return
            output.append(node.val)
            for c in node.children:
                dfs(c)
        dfs(root)
        return output

    def preorder_best_memory(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        res = [root.val]
        for node in root.children:
            res += self.preorder(node)
        return res
