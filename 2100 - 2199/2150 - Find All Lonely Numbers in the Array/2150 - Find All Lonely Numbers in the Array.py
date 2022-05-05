class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:  # 52.37% 14.62%
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        out = set()
        for num in counter:
            if counter[num] == 1 and not(num-1 in counter or num+1 in counter):
                out.add(num)
        return out

    def findLonely_best_speed(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        return [number for number, count in counts.items() if count == 1 and number - 1 not in counts and number + 1 not in counts]

    def findLonely_best_memory(self, nums: List[int]) -> List[int]:
        nums.sort()
        left = False
        res = []
        for i in range(0, len(nums) - 1):
            diff = nums[i+1] - nums[i]
            if diff > 1 and not left:
                res.append(nums[i])
            elif diff > 1 and left:
                left = False
            else:
                left = True
        if not left:
            res.append(nums[-1])
        return res
