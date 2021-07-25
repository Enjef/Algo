# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums_list) -> TreeNode:  # 70.85% 17.68%
        if not nums_list:
            return None
        mid_ind = len(nums_list) // 2
        node = TreeNode(nums_list[mid_ind])
        node.left = self.sortedArrayToBST(nums_list[:mid_ind])
        node.right = self.sortedArrayToBST(nums_list[mid_ind+1:])
        return node


def sorted_array_to_bst(nums):  # best 70.85% 59.70% 
    def construct(l, r):
        if l > r:
            return None
        if l == r:
            return TreeNode(nums[l])
        m = (l + r) // 2
        left = construct(l, m - 1)
        right = construct(m + 1, r)
        return TreeNode(nums[m], left, right)
    return construct(0, len(nums) - 1)


class Solution_best:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return sorted_array_to_bst(nums)
