class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:  # 62.58% 82.07%
        if len(nums) == 1:
            return nums
        i = 0
        j = len(nums)-1
        while i < j:
            left = nums[i] % 2 == 0
            right = nums[j] % 2 != 0
            if left:
                i += 1
            if right:
                j -= 1
            if not left and not right:
                nums[i], nums[j] = nums[j], nums[i]
        return nums

    def sortArrayByParity_best(self, nums: List[int]) -> List[int]:
        j = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums

    def sortArrayByParity_two_lists(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        even.extend(odd)
        return even
