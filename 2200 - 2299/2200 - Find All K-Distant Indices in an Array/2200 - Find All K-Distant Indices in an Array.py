class Solution:
    def findKDistantIndices(self, nums, key, k):  # 60.30% 30.76%
        out = set()
        n = len(nums)
        for i in range(n):
            if nums[i] == key:
                out.update(range(max(0, i-k), min(i+k, n-1)+1))
        return sorted(out)

    def findKDistantIndices_best_speed(self, nums, key, k):
        k_indices = [i for i, num in enumerate(nums) if num == key]
        res = []
        for i in k_indices:
            res.extend(
                range(
                    max(i - k, 0 if not res else (res[-1] + 1)),
                    min(i + k + 1, len(nums))
                ))
        return res

    def findKDistantIndices_2nd_best_speed(self, nums, key, k):
        ans = []
        lastEnd = -1
        for j, n in enumerate(nums):
            if n == key:
                ans += list(
                    range(max(lastEnd + 1, j - k), min(j + k + 1, len(nums))))
                lastEnd = j + k
        return ans

    def findKDistantIndices_best_memory(self, n, key, k):
        idx = [i for i, j in enumerate(n) if j == key]
        ans = []
        for i in range(len(n)):
            for j in idx:
                if abs(i-j) <= k:
                    ans.append(i)
                    break
        return ans
