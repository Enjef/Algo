class Solution:
    def sortJumbled(self, mapping, nums):  # 75.00% 91.67%
        def weight(target):
            arr = []
            for char in str(target):
                arr.append(str(mapping[int(char)]))
            return int(''.join(arr))
        return sorted(nums, key=weight)

    def sortJumbled_v2(self, mapping, nums):  # 83.33% 91.67%
        def weight(target):
            if not target:
                return mapping[0]
            arr = []
            while target:
                target, part = target//10, target%10
                arr.append(mapping[part])
            return int(''.join([str(x) for x in arr])[::-1])

        return sorted(nums, key=weight)

    def sortJumbled_best_speed_and_memory(self, mapping, nums):
        nums.sort(key = lambda x: int(''.join([chr(48+mapping[ord(c)-48]) for c in str(x)])))
        return nums
