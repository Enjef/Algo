class Solution:
    def triangleNumber(self, nums: List[int]) -> int:  # 5.06% 33.75%
        nums.sort()
        n = len(nums)
        result = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                left, right = j+1, n-1
                target = nums[i]+nums[j]
                cur = j
                while left <= right:
                    mid = left + (right-left)//2
                    if nums[mid] < target:
                        cur = mid
                        left = mid + 1
                    else:
                        right = mid - 1
                result += cur - j
        return result

    def triangleNumber_best_speed(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort(reverse=True)
        ans = 0
        for idx, target in enumerate(nums[:-2]):
            left, right = idx + 1, N - 1
            while left < right:
                if nums[left] + nums[right] <= target:
                    right -= 1
                else:
                    ans += right - left
                    left += 1
        return ans

    def triangleNumber_3d_best(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        for i in range(len(nums) - 1, 1, -1):
            fix = nums[i]
            start = 0
            end = i - 1
            while start < end:
                if nums[start] + nums[end] > fix:
                    res += end - start
                    end -= 1
                else:
                    start += 1
        return res

    def triangleNumber_best_memory(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        nums.sort()
        if n < 3:
            return res
        for j in range(2, n):
            i = 0
            mid = j - 1
            while i < mid:
                if nums[i] + nums[mid] > nums[j]:
                    res += mid - i
                    mid -= 1
                else:
                    i += 1
        return res
