class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:  # 75.74% 7.43%
        nums = [0] * len(flips)
        res = 0
        left = 0
        for i, flip in enumerate(flips):
            if flip-1 <= i:
                left += 1
            else:
                nums[flip-1] = 1
            left += nums[i]
            if left-1 == i:
                res += 1
        return res

    def numTimesAllBlue_best_speed(self, flips: List[int]) -> int:
        sumVal = 0
        counter = 0
        iVal = 0
        for i in range(len(flips)):
            sumVal += flips[i]
            iVal += i+1
            if sumVal == iVal:
                counter += 1
        return counter

    def numTimesAllBlue_best_memory(self, flips: List[int]) -> int:
        ans = max_light_on = 0
        for i in range(len(flips)):
            max_light_on = max(max_light_on, flips[i])
            if i+1 == max_light_on:
                ans = ans + 1
        return ans
