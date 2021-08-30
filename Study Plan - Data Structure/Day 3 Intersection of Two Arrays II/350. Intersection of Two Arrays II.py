class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_map = {}
        nums2_map = {}
        for num in nums1:
            nums1_map[num] = nums1_map.get(num, 0) + 1
        for num in nums2:
            nums2_map[num] = nums2_map.get(num, 0) + 1
        for num in nums1_map:
            nums1_map[num] = min(nums1_map.get(num, 0), nums2_map.get(num, 0))
        out = []
        for el in nums1_map:
            if nums1_map[el]:
                out.extend([el] * nums1_map[el])
        return out
