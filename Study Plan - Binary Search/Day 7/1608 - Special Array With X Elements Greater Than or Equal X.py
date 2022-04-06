class Solution:
    def specialArray(self, nums: List[int]) -> int:  # 14.08% 67.28%
        nums.sort()
        n = len(nums)
        for i in range(n+1):
            left = 0
            right = n-1
            while left <= right:
                mid = left + (right-left)//2
                if i > nums[mid]:
                    left = mid+1
                else:
                    right = mid-1
            if i == n-left:
                return i
        return -1
