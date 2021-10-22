class Solution:
    def numberOfArithmeticSlices(
            self,
            nums: List[int]) -> int:  # 60.54% 15.10%
        out = 0
        if len(nums) < 3:
            return out
        cont = 1
        for i in range(0, len(nums)-2):
            if nums[i] - nums[i+1] == nums[i+1] - nums[i+2]:
                out += 1*cont
                cont += 1
            else:
                cont = 1
        return out

    def numberOfArithmeticSlices_dp_arr(
            self,
            nums: List[int]) -> int:  # 83.84% 15.10%
        dp = [0] * len(nums)
        if len(nums) < 3:
            return 0
        for i in range(0, len(nums)-2):
            if nums[i] - nums[i+1] == nums[i+1] - nums[i+2]:
                dp[i] += dp[i-1]+1 if dp[i-1] else 1
        return sum(dp)

    def numberOfArithmeticSlices(
            self,
            nums: List[int]) -> int:  # 21.80% 90.74%
        prev = 0
        total = 0
        if len(nums) < 3:
            return 0
        for i in range(0, len(nums)-2):
            if nums[i] - nums[i+1] == nums[i+1] - nums[i+2]:
                prev += 1 
                total += prev
            else:
                prev = 0
        return total
