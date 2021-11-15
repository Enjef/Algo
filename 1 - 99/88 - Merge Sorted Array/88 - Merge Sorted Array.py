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

    def merge_best_speed(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()
