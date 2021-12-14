# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(
            self,
            root: Optional[TreeNode]) -> List[int]:  # 42.55% 80.54%
        if not root:
            return root
        out = [root.val]
        stack = [root]
        while stack:
            temp = []
            while stack:
                cur = stack.pop(0)
                if cur.left:
                    temp.append(cur.left)
                if cur.right:
                    temp.append(cur.right)
            if temp:
                out.append(temp[-1].val)
            stack = temp
        return out

    def rightSideView_best_speed(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        return self.helper(root, [], 1)
        
    def helper(self, root, nodes, lvl):
        if lvl > len(nodes):
            nodes.append(root.val)
        if root.right:
            nodes = self.helper(root.right, nodes, lvl + 1)
        if root.left:
            nodes = self.helper(root.left, nodes, lvl + 1)
        return nodes

    def rightSideView_2nd_best_speed(
            self,
            root: Optional[TreeNode]) -> List[int]:
        queue = []
        output = []
        if root:
            queue.append([root, 1])
            level = 1
            prev = root
            while queue:
                temp = queue.pop(0)                
                if temp[0].left:
                    queue.append([temp[0].left, temp[1] + 1])
                if temp[0].right:
                    queue.append([temp[0].right, temp[1] + 1])
                if temp[1] > level:
                    level = temp[1]
                    output.append(prev.val)
                prev = temp[0]
            output.append(prev.val)
        return output

    def rightSideView_best_memory(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        Q = collections.deque([root])
        while Q:
            for _ in range(len(Q)):
                node = Q.popleft()
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            res.append(node.val)
        return res
