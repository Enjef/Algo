class Solution:
    def waysToSplit(self, nums: List[int]) -> int:  # 71.24% 56.87%
        mod, pre_sum = 10**9+7, [nums[0]]
        for num in nums[1:]:
            pre_sum.append(pre_sum[-1] + num)
        ans, n = 0, len(nums)
        for i in range(n):
            prev = pre_sum[i]
            if prev * 3 > pre_sum[-1]:
                break
            j = bisect.bisect_left(pre_sum, prev * 2, i+1)
            middle = (prev + pre_sum[-1]) // 2
            k = bisect.bisect_right(pre_sum, middle, j+1)
            if k-1 >= n or pre_sum[k-1] > middle:
                continue
            ans = (ans + min(k, n - 1) - j) % mod
        return ans


from bisect import bisect_right;

class Solution_best_speed:
    def waysToSplit(self, nums: List[int]) -> int:
        psum = [0]
        for k in nums: psum.append(psum[-1] + k)
        answer = 0
        idx_l_max = min(bisect_right(psum, psum[-1]//3) - 1, len(nums)-2)
        for idx_l in range(1, idx_l_max+1):
            sum_l = psum[idx_l]
            idx_r1 = max(idx_l+1, bisect_right(psum, 2*sum_l-1))
            idx_r2 = min(bisect_right(psum, (psum[-1] + sum_l)//2), len(nums))
            answer += idx_r2 - idx_r1
        return answer % 1000000007
