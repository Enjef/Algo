# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):  #  62.87% 21.32%
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return root
        stack = [(root, 0)]
        out = [[]]
        while stack:
            root = stack.pop()
            if len(out) < root[1] + 1:
                out.append([])
            out[root[1]].append(root[0].val)
            if root[0].right:
                stack.append((root[0].right, root[1] + 1))
            if root[0].left:
                stack.append((root[0].left, root[1] + 1))
        return out

    def levelOrder_deque(self, root):  # 63.26% 96.31%
        if root is None:
            return []
        results = []
        deque = [root]
        count = 1
        while count > 0:
            cur_count = 0
            row = []
            while count > 0:
                root = deque.pop(0)
                row.append(root.val)
                count -= 1
                if root.left is not None:
                    deque.append(root.left)
                    cur_count += 1
                if root.right is not None:
                    deque.append(root.right)
                    cur_count += 1
            count = cur_count
            results.append(row)
        return results
