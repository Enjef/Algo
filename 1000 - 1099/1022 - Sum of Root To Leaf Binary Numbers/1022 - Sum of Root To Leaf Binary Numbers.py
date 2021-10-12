# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):  # 53.81%
        """
        :type root: TreeNode
        :rtype: int
        """
        way = []
        def helper(root1, arr,way):
            if not root1:
                return arr  
            if not root1.left and not root1.right:
                arr.append(way+str(root1.val))
                return arr
            helper(root1.left, arr, way+str(root1.val))
            helper(root1.right, arr, way + str(root1.val))
            return arr
        return sum(int(x, 2) for x in helper(root, [], ''))

    def sumRootToLeaf_best(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return dfs(root, 0)


def dfs(node, parent):
    if node is None:
        return 0
    parent = parent*2 + node.val
    if node.left or node.right:
        return dfs(node.left, parent) + dfs(node.right, parent)
    else:
        return parent
