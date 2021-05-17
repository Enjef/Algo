class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = []
        set1 = set(nums1)
        set2 = set(nums2)
        for i in set1:
            if i in set2:
                out.append(i)
        return out
