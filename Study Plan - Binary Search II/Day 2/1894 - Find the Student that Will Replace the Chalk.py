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
