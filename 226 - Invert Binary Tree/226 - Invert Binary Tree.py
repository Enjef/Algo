# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:  # 87.80% 11.20%
        if not root:
            return root
        cur = root
        stack = [cur]
        while stack:
            cur = stack.pop()
            cur.left, cur.right = cur.right, cur.left
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return root

    def invertTree_best(self, root: TreeNode) -> TreeNode:
        refToRoot = root
        if root is None:
            return None
        queue = [root]
        while(len(queue) != 0):
            tempQueue = []
            for i in queue:
                rightNode = i.right
                i.right = i.left
                i.left = rightNode
                if i.right is not None:
                    tempQueue.append(i.right)
                if i.left is not None:
                    tempQueue.append(i.left)
            queue = tempQueue
        return refToRoot

    def invertTree_recursive(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = (
                self.invertTree(root.right), self.invertTree(root.left)
            )
        return root
