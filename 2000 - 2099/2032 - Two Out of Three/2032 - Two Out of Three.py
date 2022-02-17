class Solution:
    def twoOutOfThree(self, nums1, nums2, nums3): # 58.64% 95.21%
        res = set()
        res.update(set(nums1) & set(nums2))
        res.update(set(nums2) & set(nums3))
        res.update(set(nums3) & set(nums1))
        return res

    def twoOutOfThree_v2(self, nums1, nums2, nums3): # 37.92% 95.21%
        return (
            set(nums1) & set(nums2) |
            set(nums2) & set(nums3) |
            set(nums3) & set(nums1)
        )

    def twoOutOfThree_best_speed(self, nums1, nums2, nums3) -> List[int]:
        return list(
            (set(nums1) & set(nums2)) |
            (set(nums2) & set(nums3)) |
            (set(nums3) & set(nums1))
        )

    def twoOutOfThree_best_memory(self, nums1, nums2, nums3) -> List[int]:
        set1, set2, set3 = set(nums1), set(nums2), set(nums3)
        ss = (set1 & set2) | (set2 & set3) | (set1 & set3) 
        return list(ss)
