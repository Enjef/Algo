class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:  # 18.82% 10.72%
        d = {}
        score = 0
        result = 0
        left = 0
        for i, num in enumerate(nums):
            score += num
            while num in d:
                score -= nums[left]
                del d[nums[left]]
                left += 1
            result = max(result, score)
            d[num] = i
        return result

    def maximumUniqueSubarray_best_speed(self, nums: List[int]) -> int:
        q, rolling, rolling_sum = deque([]), set(), 0
        maximal = 0
        for num in nums:
            if num not in rolling:
                q.append(num)
                rolling.add(num)
                rolling_sum += num
            else:
                while q[0] != num:
                    popped = q.popleft()
                    rolling.discard(popped)
                    rolling_sum -= popped
                popped = q.popleft()
                q.append(num)
            if rolling_sum > maximal:
                maximal = rolling_sum
        return maximal

    def maximumUniqueSubarray_best_memory(self, nums: List[int]) -> int:
        i = 0
        j = 0
        res = 0
        sum = 0
        mySet = set()
        while i < len(nums):
            while nums[i] in mySet:
                sum = sum - nums[j]
                mySet.remove(nums[j])
                j += 1
            if nums[i] not in mySet:
                mySet.add(nums[i])
                sum += nums[i]
                res = max(res, sum)
                i += 1
        return res
