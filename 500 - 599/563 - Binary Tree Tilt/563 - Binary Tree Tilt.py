# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:  # 89.38% 64.18%
        return sum(self.helper(root, 0, [])[1])

    def helper(self, root, cur_sum, tilt):
        if not root:
            return cur_sum, tilt
        left = self.helper(root.left, cur_sum, tilt)
        right = self.helper(root.right, cur_sum, tilt)
        tilt.append(abs(left[0] - right[0]))
        cur_sum = left[0] + right[0] + root.val
        return cur_sum, tilt

    def findTilt_best(self, root: TreeNode) -> int:
        tilt = 0
        def treeSum(root):
            nonlocal tilt
            if not root:
                return 0
            left_sum = treeSum(root.left)
            right_sum = treeSum(root.right)
            tilt += abs(left_sum - right_sum)
            return left_sum + right_sum + root.val
        treeSum(root)
        return tilt

    def findTilt_memory_best(self, root: TreeNode) -> int:
        def tilt(node):
            stackr, sumr = [node.right] if node.right else [], 0
            stackl, suml = [node.left] if node.left else [], 0

            while stackr:
                temp = stackr.pop()
                sumr += temp.val

                if temp.right:
                    stackr.append(temp.right)
                if temp.left:
                    stackr.append(temp.left)

            while stackl:
                temp = stackl.pop()
                suml += temp.val

                if temp.right:
                    stackl.append(temp.right)
                if temp.left:
                    stackl.append(temp.left)
            return abs(suml - sumr)

        if not root:
            return 0

        stackstack, sumsum = [root], 0

        while stackstack:
            temp = stackstack.pop()
            sumsum += tilt(temp)

            if temp.right:
                stackstack.append(temp.right)
            if temp.left:
                stackstack.append(temp.left)
        return sumsum
