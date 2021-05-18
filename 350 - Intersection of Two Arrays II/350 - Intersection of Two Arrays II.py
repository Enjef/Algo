class Solution:
    def intersect_first(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num_map = {}
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j] and nums1[i] not in num_map:
                num_map[nums1[i]] = 1
                i += 1
                j += 1
                continue
            if nums1[i] == nums2[j] and nums1[i] in num_map:
                num_map[nums1[i]] += 1
                i += 1
                j += 1
                continue
            if nums1[i] in num_map and nums2[j] not in num_map:
                i += 1
                continue
            if nums1[i] not in num_map and nums2[j] in num_map:
                j += 1
                continue
            if nums1[i] <= nums2[j]:
                i += 1
                continue
            if nums1[i] > nums2[j]:
                j += 1
                continue
        out = []
        print(num_map)
        for key in num_map:
            for _ in range(num_map[key]):
                out.append(key)
        return out

    def intersect_second(self, nums1, nums2):
        out = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                out.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] <= nums2[j]:
                i += 1
            else:
                j += 1
        return out
