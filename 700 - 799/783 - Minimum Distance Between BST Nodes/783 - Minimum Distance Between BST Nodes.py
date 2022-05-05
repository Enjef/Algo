class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:  # 99.42% 81.33%
        def dfs(node):
            if not node:
                return
            if node.left:
                cur = node.left
                while cur.right:
                    cur = cur.right
                self.diff = min(self.diff, node.val-cur.val)
            if node.right:
                cur = node.right
                while cur.left:
                    cur = cur.left
                self.diff = min(self.diff, cur.val-node.val)
            dfs(node.left)
            dfs(node.right)
        
        self.diff = float('inf')
        dfs(root)
        return self.diff

    def minDiffInBST_best_speed(self, root: Optional[TreeNode]) -> int:
        min_diff = float('inf')
        st = [root]
        while st:
            cur = st.pop(-1)
            if cur.left:
                node = cur.left
                while node.right:
                    node = node.right
                if node:
                    min_diff = min(
                        abs(cur.val - node.val),
                        abs(cur.val - cur.left.val), min_diff)
                else:
                    min_diff = min(abs(cur.val - cur.left.val), min_diff)
                st.append(cur.left)
            if cur.right:
                node = cur.right
                while node.left:
                    node = node.left
                if node:
                    min_diff = min(
                        abs(cur.val - node.val),
                        abs(cur.val - cur.right.val), min_diff)
                else:
                    min_diff = min (abs(cur.val - cur.left.val), min_diff)
                st.append(cur.right)
        return min_diff

    def minDiffInBST_best_memory(self, root: Optional[TreeNode]) -> int:
        result = float('inf')
        prev = float('-inf')
        node = root
        stack = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result = min(result, node.val - prev)
            prev = node.val
            node = node.right
        return result

class Solution_2nd_speed:
    def __init__(self):
        self.min_diff = float('inf')
        self.prev = None

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            inorder(node.right)

        inorder(root)    
        return self.min_diff  
