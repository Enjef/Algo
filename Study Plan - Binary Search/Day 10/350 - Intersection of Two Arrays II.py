class Solution:
    def intersect(self, nums1, nums2):  # 59.33% 88.15%
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        nums2.sort()
        res = []
        for num in nums1:
            left, right = 0, len(nums2)-1
            while left <= right:
                mid = left + (right-left)//2
                if nums2[mid] == num:
                    res.append(num)
                    nums2.pop(mid)
                    break
                if nums2[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
        return res

    def intersect_v2(self, nums1, nums2):  # 50.47% 55.16%
        nums2.sort()
        res = []
        for num in nums1:
            left, right = 0, len(nums2)-1
            while left <= right:
                mid = left + (right-left)//2
                if nums2[mid] == num:
                    res.append(num)
                    nums2.pop(mid)
                    break
                if nums2[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
        return res
