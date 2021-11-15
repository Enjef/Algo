class Solution:
    def twoSum(
            self,
            nums: List[int],
            target: int) -> List[int]:  # 22.87% 80.71%
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum_v_2(
            self,
            nums: List[int],
            target: int) -> List[int]:  # 79.67% 41.60%
        seen = {}
        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [seen[target - nums[i]], i]
            seen[nums[i]] = i
        return
