class Solution:
    # 59.96% 59.29%
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        result = 0
        for num in nums:
            if num+1 not in seen:
                cur = num
                cur_way = 0
                while cur in seen:
                    cur_way += 1
                    cur -= 1
                result = max(result, cur_way)
        return result

    def longestConsecutive_best_speed(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best

    def longestConsecutive_best_memory(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for n in nums:
            if (n-1) not in numset:
                length = 1
                while (n+length) in numset:
                    length = length + 1
                longest = max(longest, length)
        return longest
