class Solution:
    # 49.09% 40.00% (58.37% 85.93%)
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cur = 0
        res = 0
        for char in nums:
            if not char:
                cur += 1
            else:
                res += cur + cur*(cur-1)//2
                cur = 0
        res += cur + cur*(cur-1)//2
        return res


class Solution_best_speed:
    def zeroFilledSubarray_1st(self, nums: List[int]) -> int:
        ans = curr = 0
        for num in nums:
            if num == 0:
                curr += 1
                ans += curr
            else:
                curr = 0
        return ans

    def zeroFilledSubarray_2nd(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for i, n in enumerate(nums):
            if n == 0:
                count += 1
            elif n != 0 and count != 0:
                res += int(count*(count+1)/2)
                count = 0
        if count != 0:
            res += int(count*(count+1)/2)
        return res


class Solution_best_memory:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        left = ans = 0
        curr = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                curr += 1
            while left <= right and curr > 0:
                if nums[left] == 0:
                    left += 1
                else:
                    curr -= 1
                    left += 1
            ans += right - left + 1
        return ans
