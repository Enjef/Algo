class Solution:
    def minimumDifference(self, nums, k):  # 5.09% 47.75%
        nums.sort()
        n = len(nums)
        diff = float('inf')
        for i in range(n-k+1):
            diff = min(diff, max(nums[i:i+k])-min(nums[i:i+k]))
        return diff if diff != float('inf') else 0

    def minimumDifference_heap(self, nums, k) -> int:  # 99.88% 47.75%
        nums.sort()
        arr = []
        n = len(nums)
        for i in range(n-k, -1, -1):
            heappush(arr, nums[k+i-1]-nums[i])
        return heappop(arr)

    def minimumDifference_best_speed(self, nums: List[int], k: int) -> int:
        min = float('inf')
        if len(nums) <= 1:
            return 0
        nums.sort()
        for i in range(len(nums)-k+1):
            diff = nums[k-1]-nums[i]
            if diff < min:
                min = diff
            k += 1
        return min

    def minimumDifference_2nd_best_speed(self, nums: List[int], k: int) -> int:
        res = max(nums)
        nums.sort()
        i = 0
        j = k-1
        while(j < len(nums)):
            res = min(res, nums[j]-nums[i])
            i += 1
            j += 1
        return res
