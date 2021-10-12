class Solution:
    def findGCD(self, nums: List[int]) -> int:  # 27.27% 18.18%
        n_min = min(nums)
        n_max = max(nums)
        for i in range(n_min, 0, -1):
            if n_min % i == 0 and n_max % i == 0:
                return i
        return i

    def findGCD_sort(self, nums: List[int]) -> int:  # 27.27% 18.18%
        nums.sort()
        n_min = nums[0]
        n_max = nums[-1]
        def helper(a, b):
            for i in range(a, 0, -1):
                if a % i == 0 and b % i == 0:
                    return i
        return helper(n_min, n_max)
