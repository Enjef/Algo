# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int):  # 58.84% 40.95%
        def generate(n):
            if n in memo:
                return memo[n]
            res = []
            for left in range(n):
                right = n - left - 1
                left_arr, right_arr = generate(left), generate(right)
                for left_tree in left_arr:
                    for right_tree in right_arr:
                        res.append(TreeNode(0, left_tree, right_tree))
            memo[n] = res
            return memo[n]

        memo = {0: [], 1: [TreeNode()]}
        return generate(n)

    def allPossibleFBT_best_speed(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def f(n):
            if n == 0:
                return [None]
            if n % 2 == 0:
                return []
            res = []
            for i in range(n):
                l = f(i)
                r = f(n-1-i)
                for x in l:
                    for y in r:
                        res.append(TreeNode(0, x, y))
            return res
        return f(n)
