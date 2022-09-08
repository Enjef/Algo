# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.map = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:  # 85.82% 47.11%
        if not root:
            return self.map
        self.inorderTraversal(root.left)
        self.map.append(root.val)
        return self.inorderTraversal(root.right)

    def inorderTraversal_rec(
            self,
            root: Optional[TreeNode]) -> List[int]:  # 64.09% 14.30%
        def dfs(node, out):
            if not node:
                return out
            dfs(node.left, out)
            out.append(node.val)
            dfs(node.right, out)
            return out
        return dfs(root, [])

    def inorderTraversal(
            self,
            root: Optional[TreeNode]) -> List[int]:  # 19.54% 48.24%
        out = []
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if visited:
                out.append(node.val)
                continue
            if not node:
                continue
            stack.append((node.right, False))
            stack.append((node, True))
            stack.append((node.left, False))
        return out

    # 67.51% 60.15%
    def inorderTraversal_oneliner_v1(self, root: Optional[TreeNode]) -> List[int]:
        return (self.inorderTraversal(root.left) if root else []) + ([root.val] if root else []) + (self.inorderTraversal(root.right) if root else [])

    # 98.48% 60.15%
    def inorderTraversal_oneliner_v2(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

    def inorderTraversal_best_speed(
            self,
            root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return (
            self.inorderTraversal(root.left) +
            [root.val] +
            self.inorderTraversal(root.right)
        )

    def inorderTraversal_2nd_best_speed(self, root: TreeNode) -> List[int]:
        ans,ro_list = [],[]
        while ro_list or root:
            if root != None:
                ro_list.append(root)
                root = root.left
            elif ro_list != None:
                root = ro_list.pop()
                ans.append(root.val)                
                root = root.right
        return ans
