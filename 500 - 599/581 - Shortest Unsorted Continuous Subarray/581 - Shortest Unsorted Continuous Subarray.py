class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:  # 24.16% 5.86%
        new = sorted(
            [(idx, val) for idx, val in enumerate(nums)], key=lambda x: x[1])
        res = 0
        flag = False
        temp = 0
        for i in range(len(new)):
            if new[i][1] != nums[i]:
                flag = True
                if temp:
                    res += temp
                    temp = 0
                if nums[new[i][0]] == nums[i]:
                    res += 0.5
                else:
                    res += 1
            elif flag:
                temp += 1
        return res

    def findUnsortedSubarray_v2(self, nums: List[int]) -> int:  # 61.57% 90.78%
        start, end = 0, len(nums) - 1
        arr = sorted(nums)
        while start < len(nums) and nums[start] == arr[start]:
            start += 1
        while end > -1 and nums[end] == arr[end]:
            end -= 1
        return end - start + 1 if arr!=nums else 0

    def findUnsortedSubarray_best_speed(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        while (low < len(nums) - 1 and nums[low] <= nums[low + 1]):
            low += 1
        if low == len(nums) - 1:
            return 0
        while (high > 0 and nums[high] >= nums[high - 1]):
            high -= 1
        minVal = min(nums[low:high+1])
        maxVal = max(nums[low:high+1])
        while low > 0 and nums[low-1] > minVal:
            low -= 1
        while high < len(nums)-1 and nums[high+1] < maxVal:
            high += 1
        return high - low + 1

    def findUnsortedSubarray_10th_best_speed(self, nums: List[int]) -> int:
        new_a = sorted(nums)
        i = 0
        while i < len(nums) and nums[i] == new_a[i]:
            i += 1
        j = len(nums) - 1
        if i < j:
            while j >=0 and nums[j] == new_a[j]:
                j -= 1
        return j - i + 1

    def findUnsortedSubarray_best_memory(self, nums: List[int]) -> int:
        order = [x == y for x, y in zip(nums, sorted(nums))]
        return 0 if all(order) else (len(nums)) - order.index(False) - order[::-1].index(False)

    def findUnsortedSubarray_monotonic_stack(
            self, nums: List[int]) -> int:  # 71.67% 90.78%
        stack = [0]
        first = float('inf')
        last = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[stack[-1]]:
                max_index = stack[-1]
                last = i
                while stack and nums[i] < nums[stack[-1]]:
                    first = min(first, stack.pop())
                stack.append(max_index)
            else:
                stack.append(i)
        return last - first + 1 if first < last else 0
