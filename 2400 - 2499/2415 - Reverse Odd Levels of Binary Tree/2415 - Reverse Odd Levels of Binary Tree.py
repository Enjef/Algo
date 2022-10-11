# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 94.71% 98.11% (43.05% 75.38%)
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = 0
        stack = [root]
        while stack:
            new_level = []
            if level % 2:
                for i in range(len(stack)//2):
                    stack[i].val, stack[-i-1].val = stack[-i-1].val, stack[i].val
            for node in stack:
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            stack = new_level
            level += 1
        return root

    def reverseOddLevels_best_speed(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def rev(l, r):
            l.val, r.val = r.val, l.val
            if l.left and l.left.left:
                rev(l.left.left, r.right.right)
                rev(l.left.right, r.right.left)
                rev(l.right.left, r.left.right)
                rev(l.right.right, r.left.left)
        if root.left:
            rev(root.left, root.right)
        return root

    def reverseOddLevels_2nd_best_speed(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        from collections import deque
        q = deque()
        if not root.left:
            return root
        q.append(root.left)
        q.append(root.right)
        endOfTree = False
        while not endOfTree:
            start = 0
            end = len(q) - 1
            qLen = len(q)
            while end > start:
                q[start].val, q[end].val = q[end].val, q[start].val
                start += 1
                end -= 1
            if (not q[start].left or not q[start].left.left):
                break
            for i in range(qLen):
                node = q.popleft()
                q.append(node.left.left)
                q.append(node.left.right)
                q.append(node.right.left)
                q.append(node.right.right)
        return root

    def reverseOddLevels_3d_best_speed(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def rev(left_root, right_root, layer):
            if not left_root:
                return
            if layer % 2 == 1:
                left_root.val, right_root.val = right_root.val, left_root.val
            rev(left_root.left, right_root.right, layer+1)
            rev(left_root.right, right_root.left, layer+1)
            return

        rev(root.left, root.right, 1)
        return root

    def reverseOddLevels_best_memory(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        level = 0
        while q:
            if level % 2 == 1:
                l, r = 0, len(q)-1
                while l < r:
                    q[l].val, q[r].val = q[r].val, q[l].val
                    l += 1
                    r -= 1
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            level += 1
        return root
