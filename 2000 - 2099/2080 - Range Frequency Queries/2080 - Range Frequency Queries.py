# 94.37% 75.35% (94.37% 42.96%)
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.nums = defaultdict(list)
        for i, num in enumerate(arr):
            self.nums[num].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        cur = self.nums[value]
        left_q = bisect_left(cur, left)
        right_q = bisect_right(cur, right)
        return right_q - left_q


class RangeFreqQuery_best_speed:    # and second best memory
    def __init__(self, arr: List[int]):
        self.loc = defaultdict(list)
        for i, x in enumerate(arr):
            self.loc[x].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.loc:
            return 0
        lo = bisect_left(self.loc[value], left)
        hi = bisect_right(self.loc[value], right)
        return hi - lo


class RangeFreqQuery_best_memory:

    def __init__(self, arr: List[int]):
        self.arr  = arr
        self.cache = {}

    def query(self, left: int, right: int, value: int) -> int:
        if (left, right, value) in self.cache:
            return self.cache[(left, right, value)]
        else:
            sub = self.arr[left:right+1]
            count = sub.count(value)
            self.cache[(left, right, value)] = count
            return count
