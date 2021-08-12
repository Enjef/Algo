# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(
            self,
            root1: Optional[TreeNode],
            root2: Optional[TreeNode]) -> bool:  # 5.35% 42.12%
        return self.dfs(root1, []) == self.dfs(root2, [])

    def dfs(self, root, arr):
        if not root:
            return arr
        if not root.left and not root.right:
            arr.append(root.val)
            return arr
        self.dfs(root.left, arr)
        self.dfs(root.right, arr)
        return arr

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

    def compute_leaf_value_sequence(self, root: TreeNode, seq: List[int]):
        if not root:
            return
        if not root.left and not root.right:
            seq.append(root.val)
        self.compute_leaf_value_sequence(root.left, seq)
        self.compute_leaf_value_sequence(root.right, seq)

    def leafSimilar_best_speed(self, root1: TreeNode, root2: TreeNode) -> bool:
        seq1 = []
        seq2 = []
        self.compute_leaf_value_sequence(root1, seq1)
        self.compute_leaf_value_sequence(root2, seq2)
        return seq1 == seq2

    def leafSimilar_best_memory(
            self,
            root1: TreeNode,
            root2: TreeNode) -> bool:
        def bfs(root):
            stack = [(0, root)]
            res = []
            while stack:
                color, root = stack.pop()
                if root:
                    if color and not root.left and not root.right:
                        res.append(root.val)
                    elif not color:
                        stack.append((1, root))
                        stack.append((0, root.right))
                        stack.append((0, root.left))
            return res

        res1 = bfs(root1)
        res2 = bfs(root2)

        if len(res1) != len(res2):
            return False
        for i, j in zip(res1, res2):
            if i != j:
                return False
        return True
