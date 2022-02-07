# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str): # 92.14% 76.07%
        arr = traversal.split('-')
        root = TreeNode(val=int(arr[0]))
        stack = [(root, 0)]
        level = 1
        for move in arr[1:]:
            if not move:
                level += 1
                continue
            while stack[-1][1] != level - 1:
                stack.pop()
            if not stack[-1][0].left:
                stack[-1][0].left = TreeNode(val=int(move))
                stack.append((stack[-1][0].left, level))
            else:
                stack[-1][0].right = TreeNode(val=int(move))
                stack.append((stack[-1][0].right, level))
            level = 1
        return root

    def recoverFromPreorder_best_memory(self, s: str) -> Optional[TreeNode]:
        for i in range(len(s), -1, -1):
            temp='-' * i
            if s.find(temp) != 0:
                s = s.replace('-' * i, chr(i + 65))

        def helper(s, depth):
            tmp = s.split(chr(depth + 65))
            root = TreeNode(tmp[0])
            root.left = helper(tmp[1], depth+1) if len(tmp) > 1 else None
            root.right = helper(tmp[2], depth+1) if len(tmp) > 2 else None
            return root

        return helper(s, 1)
