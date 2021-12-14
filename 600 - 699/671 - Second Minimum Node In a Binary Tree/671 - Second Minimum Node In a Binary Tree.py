# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(
            self,
            root: Optional[TreeNode]) -> int:  # 58.71% 46.91%
        out = set()
        stack = [root]
        while stack:
            cur = stack.pop()
            out.add(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return sorted(out)[1] if len(out) > 1 else -1

    def findSecondMinimumValue_best_speed(
            self,
            root: Optional[TreeNode]) -> int:
        low = root.val
        q = deque([root])
        curr_set = set()
        while q:
            curr = q.pop()
            if curr.val > low:
                curr_set.add(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        min_val = -1
        if curr_set:
            min_val = min(curr_set)
        return min_val

    def findSecondMinimumValue_best_memory(
            self,
            root: Optional[TreeNode]) -> int:
        values = set()
        def traverse(root):
            if root:
                values.add(root.val)
                traverse(root.left)
                traverse(root.right)
        traverse(root)
        if len(values) == 1:
            return -1
        values.remove(root.val)
        min_val = values.pop()
        for vals in values:
            min_val = min(min_val, vals)
        return min_val
