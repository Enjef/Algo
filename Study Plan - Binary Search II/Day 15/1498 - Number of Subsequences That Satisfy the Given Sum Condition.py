class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:  # 76.06% 44.07%
        mod = 10 ** 9 + 7
        ans = 0
        nums.sort()
        for i, n in enumerate(nums):
            if 2 * n > target:
                break
            j = bisect.bisect(nums, target - n, lo=i)
            ans += pow(2, j - i - 1, mod)
        return ans % mod
