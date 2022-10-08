class Solution:
    # 69.53% 53.95% (71.98% 12.36%)
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        result = float('inf')
        for i in range(n-2):
            cur = nums[i]
            left = i + 1
            right = n-1
            while left < right:
                cur_sum = cur + nums[left] + nums[right]
                if cur_sum == target:
                    return cur_sum
                if abs(cur_sum-target) < abs(result-target):
                    result = cur_sum
                if cur_sum < target:
                    left += 1
                if cur_sum > target:
                    right -= 1
        return result

    def threeSumClosest_best_speed(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        i = 0
        while i < len(nums)-2:
            largest = nums[i] + nums[-1] + nums[-2]
            if largest < target:
                if abs(target - closest) > abs(target - largest):
                    closest = largest
                i += 1
                continue
            smallest =  nums[i] + nums[i+1] + nums[i+2]
            if smallest > target:
                if abs(target - closest) > abs(target - smallest):
                    closest = smallest
                break
            current_target = target - nums[i]
            while i > 0 and i < len(nums) - 2 and nums[i] == nums[i-1]:
                i += 1
            j = i + 1
            k = len(nums) - 1
            while j < k:
                current_sum =nums[i] + nums[j] + nums[k]
                if abs(target - closest) > abs(target - current_sum):
                    closest = current_sum
                if nums[j] + nums[k] < current_target:
                    j += 1
                elif nums[j] + nums[k] > current_target:
                    k -= 1
                else:
                    return target
            i += 1
        return closest

    def threeSumClosest_best_memory(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        closest = float('inf')
        diff = float('inf')
        for idx, num in enumerate(nums):
            low = idx + 1
            high = len(nums) - 1
            while low < high:
                curr_sum = nums[idx] + nums[low] + nums[high]
                if abs(target - curr_sum) < abs(diff):
                    diff = target - curr_sum
                    closest = curr_sum
                if curr_sum < target:
                    low += 1
                else:
                    high -= 1
                if diff == 0:
                    break
            if diff == 0:
                break
        return closest
