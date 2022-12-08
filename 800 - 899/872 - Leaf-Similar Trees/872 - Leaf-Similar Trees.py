from itertools import zip_longest


class Solution:
    # 71.32% 41.89%
    def leafSimilar_mock(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaf(root, out):
            if not root.left and not root.right:
                out.append(root.val)
            if root.left:
                leaf(root.left, out)
            if root.right:
                leaf(root.right, out)
            return out
        return leaf(root1, []) == leaf(root2, [])

    # 69.12% 42.12%
    def leafSimilar_stack(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
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

    # 88.65% 71.00%
    def leafSimilar_stack_helper(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
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

    # 78.68% 46.25% (45.41% 87.58%)
    def leafSimilar_v3(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaf_gen(node):
            if not node.left and not node.right:
                yield node.val
            else:
                if node.left:
                    yield from leaf_gen(node.left)
                if node.right:
                    yield from leaf_gen(node.right)

        return all(a == b for a, b in zip_longest(list(leaf_gen(root1)), list(leaf_gen(root2))))
        # return list(leaf_gen(root1)) == list(leaf_gen(root2)) #  13.99% 46.25% (68.58% 46.25%)

class Solution_best_speed:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]):
            if not root:
                return
            if not root.left and not root.right:
                yield root.val
                return
            yield from dfs(root.left)
            yield from dfs(root.right)

        return list(dfs(root1)) == list(dfs(root2))

    def leafSimilar_2nd(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.root1_seq = []
        self.root2_seq = []
        self.traverse(root1, self.root1_seq)
        self.traverse(root2, self.root2_seq)
        return self.root1_seq == self.root2_seq

    def traverse(self, root, lists):
        if root == None:
            return
        if root.left == None and root.right == None:
            lists.append(root.val)
            return
        self.traverse(root.left, lists)
        self.traverse(root.right, lists)


class Solution_best_memory:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaf_sequence(root: Optional[TreeNode], result=[]):
            if not root.left and not root.right:
                result.append(root.val)
            if root.left:
                get_leaf_sequence(root.left, result=result)
            if root.right:
                get_leaf_sequence(root.right, result=result)
            return result

        if (root1 and not root2) or (not root1 and root2):
            return False
        if not root1 and not root2:
            return True

        seq1 = get_leaf_sequence(root1, result=[])
        seq2 = get_leaf_sequence(root2, result=[])
        return seq1 == seq2


    def leafSimilar_2nd(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1 = []
        leaf2 = []

        def findLeafs(root, leaf):
            if not root:
                return
            if not root.left and not root.right:
                leaf.append(root.val)
                return
            findLeafs(root.left, leaf)
            findLeafs(root.right, leaf)

        findLeafs(root1, leaf1)
        findLeafs(root2, leaf2)
        if len(leaf1) != len(leaf2):
            return False
        for i in range(len(leaf1)):
            if leaf1[i] != leaf2[i]:
                return False
        return True

    def leafSimilar_best_memory_old(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node):
            if node == None:
                return []
            if node.left == None and node.right == None:
                return [node.val]
            return dfs(node.left) + dfs(node.right)
        return dfs(root1) == dfs(root2)
