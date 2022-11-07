class Solution:
    # 54.60% 95.40% (54.60% 32.77%)
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 1
        prev = nums[0]
        for num in nums:
            if num - prev <= k:
                continue
            prev = num
            res += 1
        res += int((num - prev) > k)
        return res


class Solution_best_speed:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res, j = 1, 0
        for i in range(len(nums)):
            if nums[i] - nums[j] > k:
                res += 1
                j = i
        return res


class Solution_best_memory:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        minn = nums[0]
        maxx = nums[0]
        result = 1
        for num in nums:
            if minn > num:
                minn = num
            if maxx < num:
                maxx = num
            if maxx - minn > k:
                result += 1
                minn = num
                maxx = num
        if maxx - minn > k:
            result += 1
        return result

    def partitionArray_2nd_best(self, nums: List[int], k: int) -> int:
        heapify(nums)
        ans = 0
        high = float("-inf")
        while nums:
            x = heappop(nums)
            if x > high:
                ans +=1
                high = x + k 
        return ans 
