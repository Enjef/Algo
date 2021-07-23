# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec_creation(self, arr, parent, child):  # 82.49% 63.88%
        if arr:
            max_index = arr.index(max(arr))
        else:
            return
        cur = TreeNode(arr[max_index])
        if child == 'left':
            parent.left = cur
        else:
            parent.right = cur
        self.rec_creation(arr[:max_index], cur, 'left')
        return self.rec_creation(arr[max_index+1:], cur, 'right')

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        max_index = nums.index(max(nums))
        root = TreeNode(nums[max_index])
        self.rec_creation(nums[:max_index], root, 'left')
        self.rec_creation(nums[max_index+1:], root, 'right')
        return root

    def constructMaximumBinaryTree_updated(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        max_index = nums.index(max(nums))
        root = TreeNode(nums[max_index])
        root.left = self.constructMaximumBinaryTree(nums[:max_index])
        root.right = self.constructMaximumBinaryTree(nums[max_index+1:])
        return root

    def constructMaximumBinaryTree_best(self, nums):
        nodeStack = []
        for num in nums:
            node = TreeNode(num)
            while nodeStack and num > nodeStack[-1].val:
                node.left = nodeStack.pop()
            if nodeStack:
                nodeStack[-1].right = node
            nodeStack.append(node)
        return nodeStack[0]

    def constructMaximumBinaryTree_mem_best(self, nums: List[int]) -> TreeNode:
        return self.build(nums)

    def build(self, nums):
        if not nums:
            return None
        maxNum = max(nums)
        maxNumIndex = nums.index(maxNum)
        root = TreeNode(maxNum)
        root.left = self.build(nums[:maxNumIndex])
        root.right = self.build(nums[maxNumIndex+1:])
        return root
