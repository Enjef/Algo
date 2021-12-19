class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:  # 20.57% 47.95%
        return sorted(nums)[-k]

    def findKthLargest_best_speed(self, nums: List[int], k: int) -> int:
        import heapq
        min_heap = []
        for i, num in enumerate(nums):
            heapq.heappush(min_heap, num)
            if i >= k:
                heapq.heappop(min_heap)
        return heapq.heappop(min_heap)

    def findKthLargest_best_memory(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                if num > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)
        return heap[0]
