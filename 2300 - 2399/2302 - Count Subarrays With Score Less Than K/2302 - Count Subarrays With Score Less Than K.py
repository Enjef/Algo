class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:  # 20.00% 60.00%
        left = 0
        result = 0
        cur = 0
        n = len(nums)
        for right in range(n):
            cur += nums[right]
            while cur*(right-left+1) >= k:
                cur -= nums[left]
                left += 1
            result += right-left+1
        return result

    def countSubarrays_best_memory(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ps = [0]
        for num in nums:
            ps.append(ps[-1] + num)
        ans = 0
        for l in range(n):
            lo, hi = l, n + 1
            while hi - lo > 1:
                mi = lo + hi >> 1
                if (ps[mi] - ps[l]) * (mi - l) < k:
                    lo = mi
                else:
                    hi = mi
            ans += lo - l
        return ans
