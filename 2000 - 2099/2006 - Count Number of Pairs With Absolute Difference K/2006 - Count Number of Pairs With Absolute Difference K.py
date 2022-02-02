class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int: # 77.39% 97.02% 
        seen = {}
        res = 0
        for j in range(len(nums)):
            res += seen.get(nums[j]-k, 0) + seen.get(nums[j]+k, 0)
            seen[nums[j]] = seen.get(nums[j], 0) + 1
        return res

    def countKDifference_best_speed(self, nums: List[int], k: int) -> int:
        cnt=Counter(nums)
        return sum(cnt[num]*cnt[num-k] for num in cnt if num-k in cnt )

    def countKDifference_2nd_best_speed(self, nums: List[int], k: int) -> int:
        mapNumToFrequency = {}
        result = 0
        for num in nums:
            mapNumToFrequency[num] = mapNumToFrequency.get(num, 0) + 1
        for num in nums:
            target = num + k
            result += mapNumToFrequency.get(target, 0)
        return result
