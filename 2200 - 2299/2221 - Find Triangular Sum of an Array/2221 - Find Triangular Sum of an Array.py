class Solution:
    def triangularSum(self, nums: List[int]) -> int:  # 42.61% 57.26%
        while len(nums) > 1:
            next_row = []
            for i in range(1, len(nums)):
                next_row.append((nums[i-1]+nums[i])%10)
            nums = next_row
        return nums.pop()

    def triangularSum_best_speed(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        mCk = 1
        for k, num in enumerate(nums, 1):
            result += mCk % 10 * num
            mCk = mCk * (n - k) // k
        return result % 10

    def triangularSum_best_memory(self, nums: List[int]) -> int:
        while len(nums) > 1:
            for i in range(1, len(nums)):
                nums[i-1] = (nums[i-1] + nums[i])%10
            nums.pop()
        return nums[0]
