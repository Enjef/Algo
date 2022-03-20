class Solution:
    def nextGreaterElements(self, nums):  # 5.00% 70.29%
        n = len(nums)
        nums += nums
        out = [-1] * n
        for i in range(n):
            for j in range(i, i+n):
                if nums[j] > nums[i]:
                    out[i] = nums[j]
                    break
        return out

    def nextGreaterElements_v2(self, nums):  # 99.20% 89.08%
        n = len(nums)
        out = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                out[stack.pop()] = nums[i]
            stack.append(i)
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                out[stack.pop()] = nums[i]
        return out
