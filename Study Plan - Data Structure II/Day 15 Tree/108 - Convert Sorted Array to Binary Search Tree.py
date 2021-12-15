# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(
            self,
            nums: List[int]) -> Optional[TreeNode]:  # 14.44% 60.66%
        if not nums:
            return None
        mid = (len(nums) - 1) // 2
        left = nums[:mid]
        right = nums[mid+1:]
        node = TreeNode(val=nums[mid])
        node.left = self.sortedArrayToBST(left)
        node.right = self.sortedArrayToBST(right)
        return node
