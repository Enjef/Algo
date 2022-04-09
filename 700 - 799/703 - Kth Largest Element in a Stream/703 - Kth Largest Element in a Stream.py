import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):  # 5.29 %
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        left, right = 0, len(self.nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self.nums[mid] == val:
                left = mid
                break
            elif val < self.nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        self.nums = self.nums[:left] + [val] + self.nums[left:]
        return self.nums[len(self.nums) - self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


class KthLargest_best_speed:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums.copy()
        heapq.heapify(self.heap)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]


class KthLargest_best_memory:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
