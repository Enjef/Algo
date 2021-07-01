# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum_my(self, root: TreeNode) -> int:
        res_sum = [0, 0]
        stack = [[root, 0]]
        while stack:
            root, lvl = stack.pop()
            if not root.left and not root.right:
                if lvl < res_sum[1]:
                    continue
                elif lvl > res_sum[1]:
                    res_sum = [root.val, lvl]
                else:
                    res_sum = [res_sum[0] + root.val, lvl]
            if root.left:
                stack.append([root.left, lvl + 1])
            if root.right:
                stack.append([root.right, lvl + 1])
        return res_sum[0]

    def deepestLeavesSum_best(self, root: TreeNode) -> int:
        level = [root]
        while True:
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if not next_level:
                break
            else:
                level = next_level
        return sum(node.val for node in level)
