# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.map = []

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return self.map
        self.map.append(root.val)
        self.preorderTraversal(root.left)
        return self.preorderTraversal(root.right)

    def preorderTraversal_rec(
            self,
            root: Optional[TreeNode]) -> List[int]:  # 63.73% 75.82%
        def dfs(root, out):
            if not root:
                return out
            out.append(root.val)
            if not root.left and not root.right:
                return out
            if root.left:
                dfs(root.left, out)
            if root.right:
                dfs(root.right, out)
            return out
        return dfs(root, [])

    def preorderTraversal_stack(
            self,
            root: Optional[TreeNode]) -> List[int]:  # 23.88% 75.82%
        out = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            out.append(node.val)
            stack.extend([node.right, node.left])
        return out

    def preorderTraversal_best_speed(
            self,
            root: Optional[TreeNode]) -> List[int]:
        def traverse(root=root, nodes=[]):
            if root is not None:
                nodes.append(root.val)
                traverse(root.left, nodes)
                traverse(root.right, nodes)
            return nodes
        return traverse()

    def preorderTraversal_best_memory(
            self,
            root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        stack = [root,]
        out = []
        while len(stack) > 0:
            root = stack.pop()
            if root is not None:
                out.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
        return out
