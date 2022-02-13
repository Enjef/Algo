# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root, to_delete): # 19.53% 93.68%
        stack = [(root, 0)]
        to_delete = set(to_delete)
        out = []
        while stack:
            temp = []
            while stack:
                cur, parent = stack.pop()
                if not cur:
                    continue
                if cur.val in to_delete:
                    temp.extend([(cur.left, 0), (cur.right, 0)])
                else:
                    temp.extend([(cur.left, 1), (cur.right, 1)])
                if cur.left and cur.left.val in to_delete:
                    cur.left = None
                if cur.right and cur.right.val in to_delete:
                    cur.right = None
                if not parent and cur.val not in to_delete:
                    out.append(cur)
            stack = temp
        return out
                
    def delNodes_best_speed(self, root, to_delete):
        roots = {}
        to_delete = set(to_delete)
        def delete(root):
            if root.left:
                roots[root.left.val] = root.left
            if root.right:
                roots[root.right.val] = root.right

        def dfs(root):
            if root.left and dfs(root.left):
                root.left = None
            if root.right and dfs(root.right):
                root.right = None
            if root.val in to_delete:
                delete(root)
                return True
            return False

        if not dfs(root):
            roots[root.val] = root
        return roots.values()             

    def delNodes_best_memory(self, root, to_delete):
        delete_set = set(to_delete)
        roots = [root] if root.val not in delete_set else []
        self._traverse(root, delete_set, roots)
        return roots

    def _traverse(self, cur, to_delete, roots) -> None:
        if not cur:
            return
        delete = cur.val in to_delete
        if delete:
            if cur.left and cur.left.val not in to_delete:
                roots.append(cur.left)
            if cur.right and cur.right.val not in to_delete:
                roots.append(cur.right)
        cur.left = self._traverse(cur.left, to_delete, roots)
        cur.right = self._traverse(cur.right, to_delete, roots)
        return None if delete else cur

    def delNodes_2nd_best_memory(self, root, D):
        self.ans, D = [], set(D)
        
        def dfs(node):
            if not node: return node
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node.val in D:
                for child in [node.left, node.right]:
                    if child: self.ans += [child]
                return None
            return node
                
        dfs(root)
        if root.val not in D:
            self.ans.append(root)
        return self.ans
