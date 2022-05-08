class Solution:
    def getAverages(
            self, nums: List[int], k: int) -> List[int]:  # 63.15% 53.94%
        n = len(nums)
        r = 2*k+1
        if n < r:
            return [-1] * n
        avgs = [-1] * n
        cur_sum = sum(nums[:r])
        avgs[k] = cur_sum // r
        for i in range(k+1, n-k):
            cur_sum += nums[i+k] - nums[i-k-1]
            avgs[i] = cur_sum // r
        return avgs

    def getAverages_best_speed(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        avg = [-1]*n
        if n < 2*k + 1:
            return [-1]*n
        if k == 0:
            return nums
        prevsum = sum(nums[: 2 * k + 1])
        avg[k] = prevsum // (2 * k + 1)
        for i in range(k + 1, n - k):
            prevsum -= nums[i - k - 1]
            prevsum += nums[i + k]
            avg[i] = prevsum // (2 * k + 1)
        return avg
