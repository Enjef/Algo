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
                    q_path = path + [cur]
                if not p_path and cur == p:
                    p_path = path + [cur]
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

    def lowestCommonAncestor_best_speed(
            self,
            root: 'TreeNode',
            p: 'TreeNode',
            q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ans=set()
        while p:
            ans.add(p)
            p = parent[p]
        while q not in ans:
            q = parent[q]
        return q

    def getLCA(self, root, node1, node2):
        if not root:
            return 0, root
        nodeFound = 0
        lnodeFound, lnode = self.getLCA(root.left, node1, node2)
        if lnodeFound > 1:
            return lnodeFound, lnode
        rnodeFound, rnode = self.getLCA(root.right, node1, node2)
        if rnodeFound > 1:
            return rnodeFound, rnode
        if root == node1 or root == node2:
            nodeFound += 1
        if nodeFound and (lnodeFound or rnodeFound):
            return 2, root
        elif lnodeFound == 1 and rnodeFound == 1:
            return 2, root
        return max(nodeFound, lnodeFound, rnodeFound), root

    def lowestCommonAncestor_2nd_best_speed(
            self,
            root: 'TreeNode',
            p: 'TreeNode',
            q: 'TreeNode') -> 'TreeNode':
        _, lca = self.getLCA(root, p, q)
        return lca

    def lowestCommonAncestor_3rd_best_speed(
            self,
            root: 'TreeNode',
            p: 'TreeNode',
            q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        left_res = self.lowestCommonAncestor(root.left, p, q)
        right_res = self.lowestCommonAncestor(root.right, p, q)
        if left_res and right_res:
            return root
        else:
            return left_res or right_res

    def lowestCommonAncestor_best_memory(
            self,
            root: 'TreeNode',
            p: 'TreeNode',
            q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parent = {root:None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node == None:
                return None
            if node.left != None:
                parent[node.left] = node
                stack.append(node.left)
            if node.right != None:
                parent[node.right] = node
                stack.append(node.right)
        ansester = set()
        while p:
            ansester.add(p)
            p = parent[p]
        while q not in ansester:
            q = parent[q]
        return q
