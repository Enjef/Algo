class Solution:
    def intersection(self, nums):  # 92.72% 32.05%
        out = set()
        for row in nums:
            if not out:
                out = set(row)
            else:
                out &= set(row)
        return sorted(out)

    def intersection_v2(
            self, nums: List[List[int]]) -> List[int]:  # 24.59% 66.09%
        counter = defaultdict(int)
        for row in nums:
            for num in row:
                counter[num] += 1
        return [
            key for key in sorted(counter) if counter[key]==len(nums)
        ]

    def intersection_best_speed(self, nums: List[List[int]]) -> List[int]:
        ans = set(nums[0])
        for arr in nums[1:]:
            ans = ans.intersection(set(arr))
        return sorted(list(ans))

    def intersection_2nd_best_speed(self, nums: List[List[int]]) -> List[int]:
        s = set(nums[0])
        for i in range(1, len(nums)):
            s = s & set(nums[i])
        a = list(s)
        a.sort()
        return a

    def intersection_best_memory(self, nums: List[List[int]]) -> List[int]:
        for i in range (1, len(nums)):
            for j in range(len(nums[0])-1, -1, -1):
                if not nums[0][j] in nums[i]:
                    nums[0].pop(j)
                    if not nums[0]:
                        return []
        nums[0].sort()
        return nums[0]
