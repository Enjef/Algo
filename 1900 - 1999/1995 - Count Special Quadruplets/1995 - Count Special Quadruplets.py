class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:  # 28.09% 69.35%
        total = 0
        n = len(nums)
        for a in range(n-3):
            for b in range(a+1, n-2):
                for c in range(b+1, n-1):
                    for d in range(c+1, n):
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            total += 1
        return total

    def countQuadruplets_best_speed(self, nums: List[int]) -> int:
        dct = defaultdict(int)
        n = len(nums)
        ans = 0
        for i in range(n-1):
            a = nums[i]
            for j in range(i+1, n):
                b = nums[j]
                if b-a in dct:
                    ans += dct[b-a]
            for k in range(i):
                b = nums[k]
                dct[a+b] += 1
        return ans

    def countQuadruplets_2nd_best_speed(self, nums: List[int]) -> int:
        res = 0
        seen = collections.defaultdict(int)
        for a in range(len(nums) - 1, 0, -1):
            for b in range(a - 1, -1, -1):
                res += seen[nums[a] + nums[b]]
            for d in range(len(nums) - 1, a, -1):
                seen[nums[d] - nums[a]] += 1
        return res

    def countQuadruplets_best_memory(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        for i in range(n-3):
            for j in range(i+1, n-2):
                for k in range(j+1, n-1):
                    for l in range(k+1, n):
                        if arr[l] == arr[i]+arr[j]+arr[k]:
                            ans += 1
        return ans
