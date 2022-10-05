# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 28.79% 55.00% (28.79% 93.03%)
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new = TreeNode(val, root)
            return new
        depth -= 1
        stack = [root]
        while depth:
            next_row = []
            for node in stack:
                if not node:
                    continue
                if depth == 1:
                    node_left = node.left
                    node_right = node.right
                    node.left = TreeNode(val, node_left)
                    node.right = TreeNode(val, None, node_right)
                next_row.extend([node.left, node.right])
            depth -= 1
            stack = next_row
        return root

    def addOneRow_best_speed(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        queue = [(root, 1)]
        while queue:
            node, level = queue.pop(0)
            if depth == level + 1:
                newNode = TreeNode(val)
                if node.left:
                    newNode.left = node.left
                node.left = newNode
                newNode = TreeNode(val)
                if node.right:
                    newNode.right = node.right
                node.right = newNode
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        return root
