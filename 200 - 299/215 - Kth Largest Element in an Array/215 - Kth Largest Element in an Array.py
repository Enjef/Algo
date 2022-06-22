class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:  # 65.10% 71.94%
        return sorted(nums)[-k]

    def findKthLargest_v2(self, nums: List[int], k: int) -> int:  # 56.48% 71.94%
        arr = []
        for num in nums:
            heappush(arr, -num)
        while k-1:
            heappop(arr)
            k -= 1      
        return -heappop(arr)

    def findKthLargest_best_speed(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]

    def findKthLargest_4th_best_speed(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
