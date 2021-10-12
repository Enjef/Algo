# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        out_str = ""
        r_list = [[root, out_str]]
        out = []
        while r_list:
            root, out_str = r_list.pop()
            out_str += str(root.val)
            if not root.left and not root.right:
                out.append(out_str)
            if root.left:
                r_list.append([root.left, out_str + "->"])
            if root.right:
                r_list.append([root.right, out_str + "->"])
        return out
