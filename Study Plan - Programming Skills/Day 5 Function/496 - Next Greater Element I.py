class Solution:
    def nextGreaterElement(self, nums1, nums2):  # 17.40% 97.75%
        ans = [-1]*len(nums1)
        for i, num1 in enumerate(nums1):
            for num2 in nums2[nums2.index(num1)+1:]:
                if num2 > num1:
                    ans[i] = num2
                    break
        return ans
