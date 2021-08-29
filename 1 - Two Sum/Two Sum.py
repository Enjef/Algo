class Solution:
    def twoSum(
            self,
            nums: List[int],
            target: int) -> List[int]:  # 22.87% 80.71%
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum_dict(
            self,
            nums: List[int],
            target: int) -> List[int]:  # 74.46% 40.95%
        known = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in known:
                return [known[diff], i]
            else:
                known[num] = i
