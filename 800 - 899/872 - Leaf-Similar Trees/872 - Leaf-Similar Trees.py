# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar_mock(
            self,
            root1: Optional[TreeNode],
            root2: Optional[TreeNode]) -> bool:  # 71.32% 41.89%
        def leaf(root, out):
            if not root.left and not root.right:
                out.append(root.val)
            if root.left:
                leaf(root.left, out)
            if root.right:
                leaf(root.right, out)
            return out
        return leaf(root1, []) == leaf(root2, [])

    def leafSimilar_stack(
            self,
            root1: Optional[TreeNode],
            root2: Optional[TreeNode]) -> bool:  # 69.12% 42.12%
        first = []
        second = []
        stack_first = [root1]
        stack_second = [root2]
        while stack_first or stack_second:
            if stack_first:
                cur_first = stack_first.pop()
                if not cur_first.left and not cur_first.right:
                    first.append(cur_first.val)
                if cur_first.left:
                    stack_first.append(cur_first.left)
                if cur_first.right:
                    stack_first.append(cur_first.right)
            if stack_second:
                cur_second = stack_second.pop()
                if not cur_second.left and not cur_second.right:
                    second.append(cur_second.val)
                if cur_second.left:
                    stack_second.append(cur_second.left)
                if cur_second.right:
                    stack_second.append(cur_second.right)
        return first == second

    def leafSimilar_stack_helper(
            self,
            root1: Optional[TreeNode],
            root2: Optional[TreeNode]) -> bool:  # 88.65% 71.00%
        first = []
        second = []
        stack_first = [root1]
        stack_second = [root2]
        while stack_first or stack_second:
            if stack_first:
                self.helper(stack_first, first)
            if stack_second:
                self.helper(stack_second, second)
        return first == second

    def helper(self, stack, arr):
        cur = stack.pop()
        if not cur.left and not cur.right:
            arr.append(cur.val)
        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)

    def leafSimilar_best_memory(
            self,
            root1: TreeNode,
            root2: TreeNode) -> bool:
        def dfs(node):
            if node == None:
                return []
            if node.left == None and node.right == None:
                return [node.val]
            return dfs(node.left) + dfs(node.right)
        return dfs(root1) == dfs(root2)
