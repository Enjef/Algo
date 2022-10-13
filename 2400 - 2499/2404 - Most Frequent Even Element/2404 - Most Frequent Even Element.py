class Solution:
    # 85.22% 60.02% (53.41% 99.94%)
    def mostFrequentEven(self, nums: List[int]) -> int:
        count = Counter([x for x in nums if x % 2==0])
        if not count:
            return -1
        max_q = max(count.values())
        count = sorted(x for x, y in count.items() if y == max_q)
        return count[0]

    def mostFrequentEven_best_speed(self, nums: List[int]) -> int:
        counter = collections.Counter([n for n in nums if n % 2 == 0])
        if (len(counter) == 0): return -1
        maxfrequency = max(counter.values())
        keys = list(k for k, v in counter.items() if v == maxfrequency)
        return min(keys)
