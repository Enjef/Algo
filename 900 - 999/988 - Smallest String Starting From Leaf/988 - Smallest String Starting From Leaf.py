# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(
            self, root: Optional[TreeNode]) -> str:  # 57.14% 71.43%
        def dfs(node, cur):
            if not node:
                return
            if not node.left and not node.right:
                self.small = min(self.small, (cur+[node.val])[::-1])
                return
            dfs(node.left, cur+[node.val])
            dfs(node.right, cur+[node.val])
            return

        self.small = [26] * 8500
        dfs(root, [])
        return ''.join(chr(97+x) for x in self.small)

    def smallestFromLeaf_best_speed(self, root: Optional[TreeNode]) -> str:
        self.minString = "z"*(26)

        def dfs(node, currString):
            if node:
                if node.left:
                    dfs(node.left, chr(97+node.val)+currString)
                if node.right:
                    dfs(node.right,  chr(97+node.val)+currString)
                if not node.left and not node.right:
                    self.minString = min(
                        self.minString, chr(97+node.val)+currString)

        dfs(root, "")
        return self.minString

    def smallestFromLeaf_best_memory(self, root: Optional[TreeNode]) -> str:
        self.res = None

        def dfs(root, s):
            if root:
                if root.left == root.right == None:
                    if self.res is None or self.res > s:
                        self.res = s
                if root.left:
                    ch = chr(root.left.val + ord('a'))
                    dfs(root.left, ch + s)
                if root.right:
                    ch = chr(root.right.val + ord('a'))
                    dfs(root.right, ch + s)

        ch = chr(root.val + ord('a'))
        dfs(root, ch)
        return self.res
