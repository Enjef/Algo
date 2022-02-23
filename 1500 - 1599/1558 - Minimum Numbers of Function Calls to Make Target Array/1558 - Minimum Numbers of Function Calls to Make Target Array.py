class Solution:
    def minOperations(self, nums: List[int]) -> int: # 50.00% 99.02%
        out = 0
        n = len(nums)
        while any(nums):
            for i in range(n):
                if nums[i]%2:
                    nums[i] -= 1
                    out += 1
                nums[i] //= 2
            out += 1
        return out-1 if out else out

    def minOperations_2nd_best_speed(self, nums: List[int]) -> int:
        bin_nums = [bin(num)[2:] for num in nums]
        multiplications = max(len(bin_num) for bin_num in bin_nums) - 1
        additions = sum(bin_num.count('1') for bin_num in bin_nums)
        return multiplications + additions

    def minOperations_3d_best_speed(self, nums: List[int]) -> int:
        a = [f'{i:b}' for i in nums]
        return sum(i.count('1') for i in a) + max(map(len, a)) - 1 

    def minOperations_best_memory(self, nums: List[int]) -> int:
        res = len(bin(max(nums)))-3
        return res + sum([n.bit_count() for n in nums])
