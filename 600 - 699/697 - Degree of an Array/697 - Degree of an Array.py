class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:  # 19.36% 84.19%
        n = len(nums)
        counter = {}
        for i, num in enumerate(nums):
            if num not in counter:
                counter[num] = [0, n, 0]
            counter[num][0] += 1
            counter[num][1] = min(i, counter[num][1])
            counter[num][2] = max(i, counter[num][2])
        good = max(counter.values())[0]
        candidates = [val for val in counter.values() if val[0] == good]
        result = n
        for candidate in candidates:
            result = min(result, candidate[2]-candidate[1]+1)
        return result

    def findShortestSubArray_best_speed(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1
        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)
        return ans

    # def findShortestSubArray_oneliner_TLE(self, nums: List[int]) -> int:
    # TLE
    #   return min([len(nums)-nums[::-1].index(x)-1-nums.index(x)+1 for x in [y for y in set(nums) if nums.count(y)==max([nums.count(yy) for yy in set(nums)])]])
