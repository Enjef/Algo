# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(
            self,
            root: Optional[TreeNode],
            k: int) -> int:  # 63.70% 96.42%
        out = []
        stack = [root]
        while stack:
            cur = stack.pop()
            out.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        out.sort()
        return out[k-1]

    def kthSmallest_daily(self, root, k):  # 91.37% 48.12%
        cur, stack = root, []
        while cur:
            stack.append(cur)
            cur = cur.left
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                k -= 1
                if k == 0:
                    return cur.val
                cur = cur.right
        return

    def kthSmallest_best_speed_new(self, root: Optional[TreeNode], k: int):
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

    def kthSmallest_best_speed(self, root: Optional[TreeNode], k: int) -> int:
        val, new_k = self.findK(root, k)
        if new_k != 0:
            return -1
        return val

    def findK(self, root: TreeNode, k: int) -> Tuple[int, int]:
        if not root:
            return (None, k)
        if not root.left and not root.right:
            return (root.val, k - 1)
        val, new_k = self.findK(root.left, k)
        if new_k == 0:
            return (val, new_k)
        if new_k == 1:
            return (root.val, new_k - 1)
        val, new_k = self.findK(root.right, new_k - 1)
        if new_k == 0:
            return (val, new_k)
        return (None, new_k)

    def kthSmallest_2nd_best_speed(
            self,
            root: Optional[TreeNode],
            k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
