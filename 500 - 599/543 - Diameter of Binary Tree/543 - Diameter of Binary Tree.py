# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:  # 46.19% 77.44%
        out = self.helper(root, [])[1]
        return max(out)

    def helper(self, root, arr):
        if not root:
            return 0, arr
        left = self.helper(root.left, arr)[0]
        right = self.helper(root.right, arr)[0]
        way_max = max(left, right)
        local_max = max(left + right, way_max)
        arr.append(local_max)
        return way_max + 1, arr


class Solution_best:
    diameter = -1
    def dfs(self, root):
        if(root == None):
            return -1
        left = 1 + self.dfs(root.left)
        right = 1 + self.dfs(root.right)
        self.diameter = max(self.diameter, left + right)
        return max(left, right)

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.diameter

    def diameterOfBinaryTree_best_memory_stack(self, root: TreeNode) -> int:
        res = 0
        stack = [(root, False)]
        maxHeight = {}
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    leftHeight = (
                        0 if not node.left else maxHeight.pop(node.left)
                    )
                    rightHeight = (
                        0 if not node.right else maxHeight.pop(node.right)
                    )
                    res = max(res, leftHeight + rightHeight)
                    maxHeight[node] = max(leftHeight, rightHeight) + 1
                else:
                    stack.append((node, True))
                    stack.append((node.left, False))
                    stack.append((node.right, False))
        return res
