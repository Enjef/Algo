class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:  # 51.35% 28.25%
        n = len(nums)
        i, j = nums.index(min(nums)), nums.index(max(nums))
        return min(
            max(i + 1, j + 1),
            max(n - i, n - j),
            i + 1 + n - j,
            j + 1 + n - i
        )

    def minimumDeletions_best_speed(self, nums: list[int]) -> int:
        n, m, M = len(nums), nums.index(min(nums)), nums.index(max(nums))
        return min(max(m, M)+1, n - min(m, M), 1+n-abs(m-M))

    def minimumDeletions_best_memory(self, nums: List[int]) -> int:
        n = len(nums)
        max_val_idx = nums.index(max(nums))
        min_val_idx = nums.index(min(nums))
        min_idx, max_idx = min(min_val_idx, max_val_idx), max(min_val_idx, max_val_idx)
        res = min(max_idx + 1, n - min_idx, min_idx + 1 + n - max_idx)
        return res
