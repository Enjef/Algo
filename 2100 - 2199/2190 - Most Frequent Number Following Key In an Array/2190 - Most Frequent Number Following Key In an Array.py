class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:  # 88.24% 5.88%
        count = {}
        n = len(nums)
        for i in range(n-1):
            if nums[i] == key:
                count[nums[i+1]] = count.get(nums[i+1], 0) + 1
                i += 1
        return max(count, key=count.get)

    def mostFrequent_best_speed(self, nums: List[int], key: int) -> int:
        mp = Counter()
        
        for i in range(1, len(nums)):
            if nums[i-1] == key:
                mp[nums[i]] += 1
        
        mxi = 0
        for k, v in mp.items():
            if mp[mxi] < v:
                mxi = k
        return mxi
