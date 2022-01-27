class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:  # 92.43% 96.42%
        n = len(nums)
        pos = []
        neg = []
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        j = 0
        for i in range(len(pos)):
            nums[j] = pos[i]
            j += 1
            nums[j] = neg[i]
            j += 1
        return nums

    def rearrangeArray_v2(self, nums: List[int]) -> List[int]:  # 96.71% 94.49%
        n = len(nums)
        pos = []
        neg = []
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        j = 0
        for i in range(len(pos)):
            nums[j] = pos[i]
            nums[j+1] = neg[i]
            j += 2
        return nums

    def rearrangeArray_best_speed_v1(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        neg = 1
        pos = 0
        for num in nums:
            if num < 0:
                result[neg] = num
                neg += 2
            else:
                result[pos] = num
                pos += 2
        return result

    def rearrangeArray_best_speed_v2(self, nums: List[int]) -> List[int]:
        pos = [num for num in nums if num > 0]
        neg = [num for num in nums if num < 0]
        ans = []
        for i in range(len(pos)):
            ans.append(pos[i])
            ans.append(neg[i])
        return ans
