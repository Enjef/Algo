class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m, n
        while i > 0 and j > 0:
            if nums1[i-1] >= nums2[j-1]:
                nums1[i+j-1] = nums1[i-1]
                i -= 1
            else:
                nums1[i+j-1] = nums2[j-1]
                j -= 1
        if j > -1:
            nums1[:j] = nums2[:j]


x = Solution()
# print('out', x.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
print('out', x.merge([0], 0, [1], 1))
