class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:  # 79.51% 54.75%
        n = len(nums)
        i = 0
        j = n - 1
        out = [None] * len(nums)
        k = n - 1
        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                out[k] = nums[i] * nums[i]
                i += 1
            else:
                out[k] = nums[j] * nums[j]
                j -= 1
            k -= 1
        return out

    def sortedSquares_best(self, A) -> List[int]:
        return sorted(x*x for x in A)
