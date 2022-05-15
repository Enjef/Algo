# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(
            self, root: Optional[TreeNode]) -> int:  # 90.99% 79.37%
        def dfs(node):
            if not node:
                return 0, 0
            left_sum, left_qty = dfs(node.left)
            right_sum, right_qty = dfs(node.right)
            cur_sum, cur_avrg = (
                (node.val+left_sum+right_sum),
                (1+left_qty+right_qty)
            )
            if cur_sum//cur_avrg == node.val:
                self.total += 1
            return cur_sum, cur_avrg

        self.total = 0
        dfs(root)
        return self.total

    def averageOfSubtree_best_speed(self, root: Optional[TreeNode]) -> int:
        result = [0]

        def dfs(root, result):
            if not root:
                return [0, 0]
            left = dfs(root.left, result)
            right = dfs(root.right, result)
            cur = [left[0]+right[0]+root.val, left[1]+right[1]+1]
            if (cur[0])//(cur[1]) == root.val:
                result[0] += 1
            return cur
        dfs(root, result)
        return result[0]

    def averageOfSubtree_best_memory(self, root: Optional[TreeNode]) -> int:
        def getSum(node):
            s = 0
            q = deque()
            q.append(node)
            nodes = 0
            while q:
                cur = q.popleft()
                s += cur.val
                nodes += 1
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            return s, nodes

        q1 = deque()
        q1.append(root)
        count = 0
        while q1:
            cur = q1.popleft()
            cur_sum, num_nodes = getSum(cur)
            if math.floor(cur_sum // num_nodes) == cur.val:
                count += 1
            if cur.left:
                q1.append(cur.left)
            if cur.right:
                q1.append(cur.right)
        return count
