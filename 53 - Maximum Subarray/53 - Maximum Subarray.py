class Solution:
    def maxSubArray(self, nums) -> int:
        i, j = 0, len(nums)
        a_max = float('-inf')
        while i < j:
            curr = sum(nums[i:j])
            print(curr, nums[i:j])
            if curr > a_max:
                a_max = curr
            if nums[i] < nums[j-1]:
                i += 1
            else:
                j -= 1
        return a_max


x = Solution()
print(x.maxSubArray([1,2,-1,-2,2,1,-2,1,4,-5,4]))
