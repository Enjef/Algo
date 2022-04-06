class Solution:
    def findDifference(self, nums1, nums2):  # 99.22% 60.66%
        first, second = set(nums1), set(nums2)
        return list(first-second), list(second-first)

    def findDifference_best_speed(self, nums1, nums2):
        def create_dict(x):
            dict = {}
            for i in x:
                if i not in dict:
                    dict[i] = 1
            return dict

        nums1 = create_dict(nums1)
        nums2 = create_dict(nums2)
        a = [x for x in nums1 if x not in nums2]
        b = [x for x in nums2 if x not in nums1]
        return [a, b]

    def findDifference_best_memory(self, num1, num2):
        a = list(set(num1)-set(num2))
        b = list(set(num2)-set(num1))
        return [a, b]
