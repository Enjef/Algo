class Solution:
    # 5.04% 49.87% (99.04% 49.87%)
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            arr = [0]*(len(nums)//2)
            for i in range(len(arr)):
                if i % 2:
                    arr[i] = max(nums[2*i], nums[2*i+1])
                else:
                    arr[i] = min(nums[2*i], nums[2*i+1])
            nums = arr
        return nums[0]

    def minMaxGame_best_memory(self, nums: List[int]) -> int:
        next_array = nums[:]
        while (len(next_array) > 1):
            temp_array = []
            for i in range(len(next_array)//2):
                if (i % 2 == 0):
                    temp_array.append(min(next_array[2*i], next_array[2*i+1]))
                else:
                    temp_array.append(max(next_array[2*i], next_array[2*i+1]))
            next_array = temp_array
        return next_array[0]
