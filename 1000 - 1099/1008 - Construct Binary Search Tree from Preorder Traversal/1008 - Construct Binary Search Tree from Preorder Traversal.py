# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(
            self, preorder: List[int]) -> Optional[TreeNode]:  # 95.64% 94.06%
        def add_node(value):
            node = root
            while True:
                if value < node.val:
                    if not node.left:
                        node.left = TreeNode(val=value)
                        break
                    else:
                        node = node.left
                else:
                    if not node.right:
                        node.right = TreeNode(val=value)
                        break
                    else:
                        node = node.right
            return
        root = TreeNode(val=preorder[0])
        for i in range(1, len(preorder)):
            add_node(preorder[i])
        return root

    def bstFromPreorder_best_speed(self, preorder) -> Optional[TreeNode]:
        def bisectLeft(target, lo, hi):
            while lo <= hi:
                mid = (lo + hi) // 2
                if preorder[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return lo

        def recurBuild(lo, hi):
            if lo > hi:
                return None
            nodeVal = preorder[lo]
            node = TreeNode(nodeVal)
            mid = bisectLeft(nodeVal, lo + 1, hi)
            node.left = recurBuild(lo + 1, mid - 1)
            node.right = recurBuild(mid, hi)
            return node
        return recurBuild(0, len(preorder) - 1)

    def bst(self, preorder, i, up_bound):
        if(i[0] == len(preorder) or preorder[i[0]] > up_bound):
            return None
        root = TreeNode(preorder[i[0]])
        i[0] += 1
        root.left = self.bst(preorder, i, root.val)
        root.right = self.bst(preorder, i, up_bound)
        return root

    def bstFromPreorder_best_memory(
            self, preorder: List[int]) -> Optional[TreeNode]:
        up_bound = float('inf')
        i = [0]
        ans = self.bst(preorder, i, up_bound)
        return ans

    def bstFromPreorder_2nd_best_memory(
            self, preorder: List[int]) -> Optional[TreeNode]:
        def insert(root, val):
            if not root:
                return TreeNode(val)
            if val > root.val:
                root.right = insert(root.right, val)
            else:
                root.left = insert(root.left, val)
            return root
        root = None
        for i in preorder:
            root = insert(root, i)
        return root
