class Solution:
    # 7.36% 19.89% (18.29% 67.01%)
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        res = 0
        n = len(nums)
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        res += 1
        return res


class Solution_best_speed:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = set(nums)
        ans = 0
        for i in n:
            if (i+diff) in n and (i+2*diff) in n:
                ans += 1
        return ans


class Solution_best_memory:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        triplet_count = 0
        hash_table = {}
        for i in range(len(nums)):
            hash_table[nums[i]] = i
        for i in range(1, len(nums)):
            if nums[i] - diff in hash_table and nums[i] + diff in hash_table:
                triplet_count += 1
        return triplet_count
