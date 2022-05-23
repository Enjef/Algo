class Solution:
    def reductionOperations(self, nums: List[int]) -> int:  # 63.40% 30.07%
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        keys = sorted(d)
        total = 0
        for i in range(len(d)):
            total += i*d[keys[i]]
        return total

    def reductionOperations_best_speed(self, nums: List[int]) -> int:
        c = 0
        k = -1
        nums.sort()
        prev = 0
        for n in nums:
            if n > prev:
                k = k + 1
            c = c + k
            prev = n
        return c

    def reductionOperations_best_memory(self, nums: List[int]) -> int:
        nums.sort()
        cur = nums.pop(0)
        factor = 0
        moves = 0
        while nums:
            tmp = nums.pop(0)
            if tmp > cur:
                factor += 1
            cur = tmp
            moves += factor
        return moves
