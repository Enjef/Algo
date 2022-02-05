# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:  # 66.50% 10.08%

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.root.val = 0
        self.all = set([0])
        stack = [self.root]
        while stack:
            temp = []
            while stack:
                cur = stack.pop(0)
                if cur.left:
                    cur.left.val = cur.val * 2 + 1
                    self.all.add(cur.left.val)
                    temp.append(cur.left)
                if cur.right:
                    cur.right.val = cur.val * 2 + 2
                    self.all.add(cur.right.val)
                    temp.append(cur.right)
            stack = temp
        return

    def find(self, target: int) -> bool:
        return target in self.all


class FindElements_best_speed:
    def __init__(self, root: Optional[TreeNode]):
        self.elements = set()
        def helper(node, val):      # explore tree from node with correct value val
            if not node:
                return
            self.elements.add(val)
            helper(node.left, 2 * val + 1)
            helper(node.right, 2 * val + 2)
        helper(root, 0)

    def find(self, target: int) -> bool:
        return target in self.elements


class FindElements_best_memory:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.exists = set()

    def find(self, target: int) -> bool:
        if target in self.exists:
            return True
        path = []
        while target != 0:
            even = (target % 2) == 0
            if even:
                target = (target - 2)//2
                path.append(0)
            else:
                target = (target - 1)//2
                path.append(1)
        root = self.root
        val = 0
        while len(path) != 0:
            move = path.pop()
            if move == 0:
                root = root.right
                val = val*2 + 2
            else:
                root = root.left
                val = val*2 + 1
            if root is None:
                return False
            self.exists.add(val)
        return True
