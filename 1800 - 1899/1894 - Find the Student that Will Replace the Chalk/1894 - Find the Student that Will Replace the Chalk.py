class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:  # 91.95% 44.16%
        k = k % sum(chalk)
        for i, cur in enumerate(chalk):
            if k < cur:
                return i
            k -= cur
        return -1

    def chalkReplacer_bin_search(self, chalk, k):  # 87.27% 6.75%
        k = k % sum(chalk)
        n = len(chalk)
        for i in range(1, n):
            chalk[i] += chalk[i-1]
        left, right = 0, n-1
        while left < right:
            mid = left + (right-left)//2
            if chalk[mid] > k:
                right = mid
            else:
                left = mid + 1
        return left

    def chalkReplacer_best_speed(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        for i, a in enumerate(chalk):
            if k < a:
                return i
            k -= a
        return 0

    def chalkReplacer_best_bin_search(self, chalk: List[int], k: int) -> int:
        sums = sum(chalk)
        l = 0
        r = k//sums + 1
        while l < r:
            mid = (l+r) // 2
            if sums * mid > k:
                r = mid
            else:
                l = mid + 1
        k -= sums*(l-1)
        pos = 0
        while k >= 0:
            if chalk[pos] <= k:
                k -= chalk[pos]
                pos += 1
            else:
                return pos
