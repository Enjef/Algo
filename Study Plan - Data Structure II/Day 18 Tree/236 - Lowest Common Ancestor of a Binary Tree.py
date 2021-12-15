# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(
            self,
            root: 'TreeNode',
            p: 'TreeNode',
            q: 'TreeNode') -> 'TreeNode':  # 5.42% 94.80%
        p_path = []
        q_path = []
        stack = [(root, [])]
        while stack:
            temp = []
            while stack:
                cur, path = stack.pop()
                if not q_path and cur == q:
                    q_path = path+[cur]
                if not p_path and cur == p:
                    p_path = path+[cur]
                if q_path and p_path:
                    temp = []
                    break
                if cur.left:
                    temp.append((cur.left, path+[cur]))
                if cur.right:
                    temp.append((cur.right, path+[cur]))
            stack = temp
        q_path = set(q_path)
        for node in p_path[::-1]:
                if node in q_path:
                    return node
