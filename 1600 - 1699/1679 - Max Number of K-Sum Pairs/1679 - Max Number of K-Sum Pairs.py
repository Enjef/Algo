class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:  # 17.86% 33.48%
        counter = defaultdict(int)
        result = 0
        for num in nums:
            counter[num] += 1
        for num in counter:
            target = k-num
            if target == num:
                result += counter[num]//2
                counter[num] = ceil(counter[num]//2)
            elif target in counter:
                pairs = min(counter[num], counter[target])
                result += pairs
                counter[num] -= pairs
                counter[target] -= pairs
        return result

    def maxOperations_v2_pointers(
            self, nums: List[int], k: int) -> int:  # 76.79% 71.21%
        nums.sort()
        n = len(nums)
        left, right = 0, n-1
        result = 0
        while left < right:
            cur = nums[left] + nums[right]
            if cur == k:
                result += 1
                left += 1
                right -= 1
            elif cur < k:
                left += 1
            else:
                right -= 1
        return result

    def maxOperations_v2(self, nums, k):  # 50.90% 33.48%
        counter = defaultdict(int)
        result = 0
        for num in nums:
            counter[num] += 1
        for num in counter:
            target = k-num
            if target < 0:
                continue
            if target == num:
                result += counter[num]//2
                counter[num] = ceil(counter[num]//2)
            elif target in counter:
                pairs = min(counter[num], counter[target])
                result += pairs
                counter[num] -= pairs
                counter[target] -= pairs
        return result

    def maxOperations_v3(self, nums: List[int], k: int) -> int:  # 22.33% 17.63%
        counter = defaultdict(int)
        result = 0
        for num in nums:
            counter[num] += 1
        for num in counter:
            target = k-num
            if target in counter:
                pairs = min(counter[num], counter[target])
                if num == target:
                    pairs //= 2
                result += pairs
                counter[num] -= pairs
                counter[target] -= pairs
        return result

    def maxOperations_best_speed(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        ans = 0
        for c in counter:
            o = k-c
            if c < o:
                ans += min(counter[c], counter[o])
            elif c == o:
                ans += counter[c]//2
        return ans

    def maxOperations_3d_best_speed(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        res = 0
        while counter:
            n, c = counter.popitem()
            complement = k - n
            if complement == n:
                res += c // 2
            elif complement in counter:
                res += min(c, counter[complement])
                counter.pop(complement)
        return res

    def maxOperations_best_memory(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        count = 0
        while l < r:
            if nums[l] + nums[r] < k:
                l += 1
            elif nums[l] + nums[r] > k:
                r -= 1
            else:
                count += 1
                nums.pop(r)
                nums.pop(l)
                r -= 2
        return count
