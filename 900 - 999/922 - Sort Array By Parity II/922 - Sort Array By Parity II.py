class Solution:
    def sortArrayByParityII(
            self,
            nums: List[int]) -> List[int]:  # 48.06% 29.54%
        odd = []
        even = []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return [el for tup in zip(even, odd) for el in tup]

    def sortArrayByParityII_best_speed(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        even_indx, odd_indx = 0, 1
        for num in nums:
            if num % 2 == 0:
                ans[even_indx] = num
                even_indx += 2
            else:
                ans[odd_indx] = num
                odd_indx += 2
        return list(ans)

    def sortArrayByParityII_memory(self, nums: List[int]) -> List[int]:
        i, j, s = 0, 1, len(nums)
        while i < s and j < s:
            if not nums[i] % 2:
                i += 2
            elif(nums[j] % 2):
                j += 2
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                j += 2
        return nums
