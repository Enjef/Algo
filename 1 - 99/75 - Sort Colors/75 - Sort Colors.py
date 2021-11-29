class Solution:
    def sortColors_ds_2_day_2(self, nums: List[int]) -> None:  # 48.58% 13.35%
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        one = 0
        two = 0
        for num in nums:
            if num == 0:
                zero = zero + 1
            elif num == 1:
                one = one + 1
            else:
                two = two + 1
        nums[:] = [0] * zero + [1] * one + [2] * two
        return

    def sortColors_best_speed(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0 for _ in range(3)]
        for i in nums:
            freq[i] += 1
        count = 0
        for k in range(len(freq)):
            v = freq[k]
            for i in range(count, count+v):
                nums[i] = k
            count += v

    def sortColors_2nd_best_speed(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0]*3
        for n in nums:
            count[n] += 1
        for i in range(1,3):
            count[i] += count[i-1]
        res = nums[:]
        for n in res:
            nums[count[n]-1] = n
            count[n] -= 1

    def sortColors_3nd_best_speed(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r, w, b = 0, 0, len(nums) - 1
        while w <= b:
            if nums[w] == 0:
                nums[w], nums[r] = nums[r], nums[w]
                w += 1
                r += 1
            elif nums[w] == 2:
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1
            else:
                w += 1

    def sortColors_best_memory(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first = 0
        second  = len(nums) - 1
        current = 0
        while current <= second:
            if nums[current] == 0:
                nums[current], nums[first] = nums[first], nums[current]
                first = first + 1
                current = current + 1
            elif nums[current] == 1:
                current = current + 1       
            elif nums[current] == 2:
                nums[current], nums[second] = nums[second], nums[current]
                second = second - 1
