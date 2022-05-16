class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:  # 62.05% 6.03%
        nums = [(-int(x), x) for x in nums]
        heapify(nums)
        while k-1:
            heappop(nums)
            k -= 1
        return heappop(nums)[1]

    def kthLargestNumber_v2(self, nums, k):  # 20.41% 79.39%
        nums.sort(key=int)
        return nums[-k]

    def kthLargestNumber_best_speed(self, nums: List[str], k: int) -> str:
        nums.sort()
        nums.sort(key=lambda t: len(t))
        return nums[len(nums) - k]

    def kthLargestNumber_2nd_best_speed(self, nums: List[str], k: int) -> str:
        dc = defaultdict(list)
        for n in nums:
            dc[len(n)].append(n)
        arr = []
        for length in sorted(dc.keys()):
            arr.extend(sorted(dc[length]))
        return arr[len(nums)-k]

    def kthLargestNumber_3d_best_speed(self, nums: List[str], k: int) -> str:
        arr = []
        for num in nums:
            arr.append(int(num))
        arr.sort()
        return str(arr[-k])

    def kthLargestNumber_best_memory(self, nums: List[str], k: int) -> str:
        maxHeap = []       
        while(nums):
            num=int(nums.pop(0))
            heapq.heappush(maxHeap,-num)
        while(k>1):
            heapq.heappop(maxHeap)
            k-=1
        return str(-1*heapq.heappop(maxHeap))

    def kthLargestNumber_2dn_best_memory(self, nums: List[str], k: int) -> str:
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        return str(sorted(nums,reverse=True)[k-1])
