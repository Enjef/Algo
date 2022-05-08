class Solution:
    def countHillValley(self, nums: List[int]) -> int:  # 10.78% 73.88%
        prev = nums[0]
        n = len(nums)
        total = 0
        for i in range(1, n-1):
            if prev != nums[i] and nums[i] == nums[i+1]:
                continue
            if (
                    prev < nums[i] > nums[i+1] or
                    prev > nums[i] < nums[i+1]):
                total += 1
            prev = nums[i]
        return total

    def countHillValley_best_speed(self, nums: List[int]) -> int:
        l = len(nums)
        arr = []
        arr.append(nums[0])
        for i in range(1, l):
            if nums[i] != nums[i-1]:
                arr.append(nums[i])
        count = 0
        for i in range(1, len(arr)-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1] or arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                count += 1
        return count

    def countHillValley_best_memory(self, nums: List[int]) -> int:
        res = 0
        j = 0
        for i in range(1, len(nums)-1, 1):
            if ((nums[j] < nums[i] and nums[i] > nums[i + 1]) or
                    (nums[j] > nums[i] and nums[i] < nums[i + 1])):
                res += 1
                j = i
        return res
