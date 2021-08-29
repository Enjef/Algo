class Solution:
    def merge(
            self,
            nums1: List[int],
            m: int,
            nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums1)-1, -1, -1):
            if not nums2:
                return nums1
            if m == 0:
                nums1[:len(nums2)] = nums2[:len(nums2)]
                return
            if nums1[m-1] > nums2[-1]:
                nums1[i] = nums1[m-1]
                m -= 1
            else:
                nums1[i] = nums2.pop()
