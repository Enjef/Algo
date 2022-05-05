class Solution:
    def largestSumAfterKNegations_my(self, nums, k):  # 27.18% memory 82.77%
        for _ in range(k):
            nums[nums.index(min(nums))] *= -1
        return sum(nums)

    def largestSumAfterKNegations_heap(
            self, nums: List[int], k: int) -> int:  # 88.30% 93.78%
        heapify(nums)
        for i in range(k):
            heappush(nums, -heappop(nums))
        return sum(nums)

    def largestSumAfterKNegations_best_speed(self, nums, k):
        possave = []
        negsave = []
        allpossave = []
        for i in nums:
            allpossave.append(abs(i))
        for i in nums:
            if i >= 0:
                possave.append(i)
            else:
                negsave.append(i)
        possave.sort()
        negsave.sort()
        allpossave.sort()
        if len(negsave) == 0:
            if k % 2 == 0:
                sums = sum(nums)
            else:
                sums = sum(nums)-2*min(nums)
        else:
            if len(negsave) >= k:
                sums = sum(possave) + abs(sum(negsave[0:k])) + sum(negsave[k:])
            else:
                if (k-len(negsave)) % 2 == 0:
                    sums = sum(allpossave)
                else:
                    sums = sum(allpossave) - 2 * allpossave[0]
        return sums

    def largestSumAfterKNegations_2nd_best_speed(self, nums, k):
        l = sorted(nums, key=abs, reverse=True)
        for i in range(len(l)):
            if k > 0 and l[i] < 0:
                l[i] *= -1
                k -= 1
        if k > 0:
            l[-1] *= (-1)**k
        return sum(l)

    def largestSumAfterKNegations_2nd_best_memory(self, nums, k):
        nums.sort()
        while (k > 0):
            nums.sort()
            if (k == 0):
                break
            nums[0] = nums[0] * -1
            k -= 1
        return sum(nums)
