class Solution:
    def minSubArrayLen(self, target, nums):  # 14.98% 53.81%
        n = len(nums)
        if n == 1:
            return int(nums[0] >= target)
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        if nums[-1] < target:
            return 0
        out = n+1
        for i in range(n):
            left, right = i, n-1
            if nums[i] >= target:
                out = min(out, i+1)
            while left < right:
                mid = left + (right-left)//2
                cur = nums[mid]-nums[i]
                if cur >= target:
                    right = mid
                else:
                    left = mid + 1
            if nums[left]-nums[i] >= target:
                out = min(out, left-i)
        if out == n+1 and nums[-1] == target:
            out = n
        return out if out != n+1 else 0
