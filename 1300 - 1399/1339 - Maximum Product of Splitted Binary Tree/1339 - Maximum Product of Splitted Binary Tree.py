# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    # 82.99% 77.58% ()
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs_sum(node):
            if not node:
                return
            self.total += node.val
            dfs_sum(node.left)
            dfs_sum(node.right)

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            cur = node.val + left + right
            self.result = max(self.result, (self.total-cur)*cur)
            return cur

        mod = 10**9 + 7
        self.result = 0
        self.total = 0
        dfs_sum(root)
        dfs(root)
        return self.result % mod


class Solution_best_speed:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def helper(curr):
            if curr is None:
                return 0
            curr.val += helper(curr.left) + helper(curr.right)
            return curr.val

        sumnum = helper(root)
        curr = root
        ans = 0
        while curr is not None and curr.val >= sumnum / 2:
            another = sumnum - curr.val
            ans = max(ans, another * curr.val)
            left = right = 0
            if curr.left is not None:
                left = curr.left.val
            if curr.right is not None:
                right = curr.right.val
            if left > right:
                curr = curr.left
            else:
                curr = curr.right
        if curr is None:
            return ans
        newans = curr.val * (sumnum - curr.val)
        return max(newans, ans) % (pow(10, 9) + 7)

    def maxProduct_2nd(self, root: Optional[TreeNode]) -> int:
        tree_sums = []

        def tree_sum(node):
            if node is None:
                return 0
            ans = node.val + tree_sum(node.left) + tree_sum(node.right)
            tree_sums.append(ans)
            return ans

        total = tree_sum(root)
        mx_prod = max([(total - s) * s for s in tree_sums])
        return mx_prod % (10**9 + 7)


class Solution_best_memory:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sm = 0
        stack = [root]
        subtree = defaultdict(lambda: -1)
        while stack:
            a = stack[-1]
            if subtree[a] == -1:
                subtree[a] = a.val
                sm += a.val
                if a.left != None:
                    stack.append(a.left)
                if a.right != None:
                    stack.append(a.right)
            else:
                a = stack.pop()
                if a.left != None:
                    subtree[a] += subtree[a.left]
                if a.right != None:
                    subtree[a] += subtree[a.right]
        ans = 0
        stack = [root]
        while stack:
            a = stack.pop()
            if a.left != None:
                stack.append(a.left)
                ans = max(ans, (sm-subtree[a.left])*subtree[a.left])
            if a.right != None:
                stack.append(a.right)
                ans = max(ans, (sm-subtree[a.right])*subtree[a.right])
        return ans % ((10**9)+7)

    def maxProduct_2nd(self, root: Optional[TreeNode]) -> int:
        possible_sums = {}
        todo = deque([(root, 'start')])
        while todo:
            nxt = todo.pop()
            if nxt[1] == 'start':
                todo.append((nxt[0], 'end'))
                if nxt[0].left:
                    todo.append((nxt[0].left, 'start'))
                if nxt[0].right:
                    todo.append((nxt[0].right, 'start'))
            else:
                s = nxt[0].val
                if nxt[0].left:
                    s += possible_sums[id(nxt[0].left)]
                if nxt[0].right:
                    s += possible_sums[id(nxt[0].right)]
                possible_sums[id(nxt[0])] = s
        total = possible_sums[id(root)]
        del possible_sums[id(root)]
        sums = list(possible_sums.values())
        sums.sort()
        i = bisect.bisect_left(sums, total/2)
        test = 0
        if i < len(sums):
            test = (sums[i]*(total-sums[i]))
        if i-1 >= 0:
            test = max(test, (sums[i-1]*(total-sums[i-1])))
        return test % (10**9 + 7)

    def maxProduct_3d(self, root: Optional[TreeNode]) -> int:
        self.total_sum = self.ret = 0

        def post_order(root):
            if not root: 
                return 0
            left_sum, right_sum = post_order(root.left), post_order(root.right)
            self.ret = max(self.ret, left_sum * (self.total_sum - left_sum), right_sum * (self.total_sum - right_sum))

            return root.val + left_sum + right_sum

        self.total_sum = post_order(root)
        _ = post_order(root)

        return self.ret % (10**9 + 7)
