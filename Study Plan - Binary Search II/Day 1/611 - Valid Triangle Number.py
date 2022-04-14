class Solution:
    def triangleNumber(self, nums: List[int]) -> int:  # 5.06% 33.75%
        nums.sort()
        n = len(nums)
        result = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                left, right = j+1, n-1
                target = nums[i]+nums[j]
                cur = j
                while left <= right:
                    mid = left + (right-left)//2
                    if nums[mid] < target:
                        cur = mid
                        left = mid + 1
                    else:
                        right = mid - 1
                result += cur - j
        return result
