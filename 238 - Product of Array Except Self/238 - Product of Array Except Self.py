class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:  # 78.66% 49.37%
        out = []
        prod = 1
        if nums.count(0) > 1:
            return [0]*len(nums)
        for num in nums:
            prod *= num
        for num in nums:
            temp = 1
            if num == 0:
                for num in nums[:nums.index(0)]+nums[nums.index(0)+1:]:
                    temp *= num
            else:
                temp = prod // num
            out.append(temp)
        return out

    def productExceptSelf_best_speed(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        L = len(output)
        for i in range(1, L):
            output[i] = output[i-1] * nums[i-1]
        r = 1
        for i in reversed(range(L)):
            output[i] = output[i] * r
            r = r * nums[i]
        return output
