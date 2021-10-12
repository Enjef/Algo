class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:  # 5.14% 78.02 %
        sum_max = cur_max = float('-inf')
        cur_min = sum_min = float('inf')
        all_negative = True
        for num in nums:
            if num > 0:
                all_negative = False
                break
        if all_negative:
            return max(nums)
        total = sum(nums)
        for num in nums:
            cur_min = min(cur_min + num, num)
            sum_min = min(sum_min, cur_min)
            cur_max = max(cur_max + num, num)
            sum_max = max(sum_max, cur_max)
        if sum_min < 0:
            total -= sum_min
        return max(total, sum_max)

    def maxSubarraySumCircular_best_speed(self, nums: List[int]) -> int:
        total_sum = 0
        complete_max = nums[0]
        min_sum = current_min_sum = current_max_sum = max_sum = 0
        for e in nums:
            total_sum += e
            current_min_sum += e
            if e > complete_max:
                complete_max = e
            if current_min_sum > 0:
                current_min_sum = 0
            elif current_min_sum < min_sum:
                min_sum = current_min_sum
            current_max_sum += e
            if current_max_sum < 0:
                current_max_sum = 0
            elif current_max_sum > max_sum:
                max_sum = current_max_sum
        result = max(total_sum - min_sum, max_sum)
        return complete_max if result == 0 else result

    def maxSubarraySumCircular_best_memory(self, nums: List[int]) -> int:
        minsum, maxsum = nums[0], nums[0]
        currmin, currmax = 0, 0
        total = 0
        for num in nums:
            currmax = num + max(0, currmax)
            maxsum = max(maxsum, currmax)
            currmin = num + min(0, currmin)
            minsum = min(minsum, currmin)
            total += num
        return max(maxsum, total - minsum) if maxsum > 0 else maxsum
