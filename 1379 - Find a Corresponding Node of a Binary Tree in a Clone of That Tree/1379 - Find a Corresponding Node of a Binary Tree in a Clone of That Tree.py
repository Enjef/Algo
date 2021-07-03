# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy_my(self, original, cloned, target):
        ori = [original]
        clo = [cloned]
        while ori:
            cur_ori = ori.pop()
            cur_clo = clo.pop()
            if cur_ori == target:
                return cur_clo
            if cur_ori.left:
                ori.append(cur_ori.left)
                clo.append(cur_clo.left)
            if cur_ori.right:
                ori.append(cur_ori.right)
                clo.append(cur_clo.right)

    def getTargetCopy_best(self, original, cloned, target):
        q = [cloned]
        while q:
            node = q.pop(0)
            if node.val == target.val:
                return node
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return None
