class Solution:
    # 84.13% 39.95%
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        for query in queries:
            ans.append(bisect_right(nums, query))
        return ans

    def answerQueries_best_speed(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return [bisect_right(nums, q) for q in queries]

    def answerQueries_best_memory(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []
        nums.sort()
        for ele in queries:
            s = 0
            count = 0
            for i in range(len(nums)):
                s += nums[i]
                if s <= ele:
                    count += 1
            ans.append(count)
        return ans
