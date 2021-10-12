# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent_my(self, root: TreeNode) -> int:  #  66.60%
        stack = [(root, 0, [])]
        out = 0
        while stack:
            root = stack.pop()
            if root[0].val % 2 == 0:
                root[2].append(root[1]+2)
            if root[1] in root[2]:
                out += root[0].val
            if root[0].left:
                stack.append((root[0].left, root[1]+1, root[2][:]))
            if root[0].right:
                stack.append((root[0].right, root[1]+1, root[2][:]))
        return out

    def sumEvenGrandparent_best(self, root: TreeNode) -> int:
        res_sum = 0

        def findSum(curr, parent, gParent):
            nonlocal res_sum
            if gParent and not gParent.val % 2:
                res_sum += curr.val
            if curr.left:
                findSum(curr.left, curr, parent)
            if curr.right:
                findSum(curr.right, curr, parent)
        findSum(root, None, None)
        return res_sum
