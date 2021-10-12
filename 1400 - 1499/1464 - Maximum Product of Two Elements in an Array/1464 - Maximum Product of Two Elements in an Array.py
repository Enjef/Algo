class Solution:
    def maxProduct(self, nums: List[int]) -> int:  # 94.68% 45.38%
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)

    def maxProduct_best(self, nums: List[int]) -> int:
        heapq._heapify_max(nums)
        return (heapq._heappop_max(nums)-1)*(heapq._heappop_max(nums)-1)
