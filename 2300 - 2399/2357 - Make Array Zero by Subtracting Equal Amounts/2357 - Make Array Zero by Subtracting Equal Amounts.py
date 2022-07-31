class Solution:
    # 25.00% 75.00%
    def minimumOperations(self, nums: List[int]) -> int:
        set_nums = set(nums)
        if sorted(set_nums)[0] == 0:
            return len(set_nums)-1
        else:
            return len(set_nums)

    def minimumOperations_best_speed(self, nums: List[int]) -> int:
        return len(set(x for x in nums if x))

    def minimumOperations_best_memory(self, nums: List[int]) -> int:
        return len(set(nums)) - int(0 in nums)
