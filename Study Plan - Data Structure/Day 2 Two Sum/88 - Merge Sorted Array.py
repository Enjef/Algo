class Solution:
    def merge(
            self,
            nums1: List[int],
            m: int,
            nums2: List[int], n: int) -> None:  # 75.29%
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

    def merge_v_2(
            self,
            nums1: List[int],
            m: int,
            nums2: List[int], n: int) -> None:  # 75.29% 96.27%
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return
        if not nums1:
            nums1.extend(nums2)
            return
        j = m - 1
        k = n - 1
        for i in range(m+n-1,-1,-1):
            if (nums1[j] < nums2[k] or j < 0) and k > -1:
                nums1[i] = nums2[k]
                k -= 1
            else:
                nums1[i] = nums1[j]
                j -= 1
        return
