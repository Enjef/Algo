# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:  # 45.98% 6.57%
        def dfs(node, counter):
            if not node:
                return
            if counter[node.val]:
                counter[node.val] = 0
            else:
                counter[node.val] += 1
            if not node.left and not node.right:
                self.result += sum([x % 2 for x in counter.values()]) < 2
                return
            dfs(node.left, counter.copy())
            dfs(node.right, counter.copy())
            return

        self.result = 0
        dfs(root, defaultdict(int))
        return self.result

    def pseudoPalindromicPaths_best_speed(self, root: Optional[TreeNode]) -> int:
        def dfs(root, path):
            nonlocal ans
            if root is None:
                return
            path ^= (1 << root.val)
            if root.left is None and root.right is None:
                if path & (path - 1) == 0:
                    ans += 1
                return
            dfs(root.left, path)
            dfs(root.right, path)

        ans = 0
        dfs(root, 0)
        return ans

    def pseudoPalindromicPaths_4th_best_sped(
            self, root: Optional[TreeNode]) -> int:
        def dfs(root, curr):
            if not root:
                return
            if root.val in curr:
                curr.remove(root.val)
            else:
                curr.add(root.val)
            if not root.left and not root.right:
                if len(curr) <= 1:
                    self.ans += 1
            else:
                dfs(root.left, curr)
                dfs(root.right, curr)
            if root.val in curr:
                curr.remove(root.val)
            else:
                curr.add(root.val)

        self.ans = 0
        dfs(root, set())
        return self.ans

    def pseudoPalindromicPaths_best_memory(
            self, root: Optional[TreeNode]) -> int:
        count = 0
        stack = [(root, set())]
        while stack:
            node, seen = stack.pop()
            seen = seen.copy()
            if node.val in seen:
                seen.remove(node.val)
            else:
                seen.add(node.val)
            children = [node.left, node.right]
            if children == [None, None] and len(seen) <= 1:
                count += 1
            for child in children:
                if child is not None:
                    stack.append((child, seen))
        return count
