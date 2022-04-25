class Solution:
    def rangeSum(self, nums, n, left, right):  # 86.55% 29.83%
        arr = []
        n = len(nums)
        for i in range(n):
            cur = nums[i]
            arr.append(cur)
            for j in range(i+1, n):
                cur += nums[j]
                arr.append(cur)
        arr.sort()
        return sum(arr[left-1:right]) % (10**9+7)

    def rangeSum_best_speed(self, nums, n, left, right):
        mod = 10 ** 9 + 7

        def caterpillar(target):
            lp = 0
            rank = 0
            sum_of_subarray_sums = 0
            windowsum = 0
            elements = 0
            prefixsum = 0
            for num in nums:
                elements += 1
                windowsum += elements * num
                prefixsum += num
                while prefixsum > target:
                    windowsum -= prefixsum
                    prefixsum -= nums[lp]
                    elements -= 1
                    lp += 1
                rank += elements
                sum_of_subarray_sums += windowsum
            return rank, sum_of_subarray_sums

        max_sum = sum(nums)

        def bi_search(target_rank):
            if not target_rank:
                return 0
            lp = 1
            up = max_sum
            memo = [(0, 0), None]
            while lp != up:
                mp = (lp + up) // 2
                rank, subarraysum_total = caterpillar(mp)
                if rank < target_rank:
                    lp = mp + 1
                    memo[0] = (rank, subarraysum_total)
                else:
                    up = mp
                    memo[1] = (rank, subarraysum_total)
            if memo[1] is None:
                memo[1] = caterpillar(up)
            if memo[1][0] == target_rank:
                return memo[1][1]
            (r0, t0), (r1, t1) = memo
            delta = (t1 - t0) // (r1 - r0)
            return t0 + (target_rank - r0) * delta
        return (bi_search(right) - bi_search(left - 1)) % mod
