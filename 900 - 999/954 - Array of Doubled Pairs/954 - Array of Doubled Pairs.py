class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        counter = {}
        for num in arr:
            counter[num] = counter.get(num, 0) + 1
        counter[0] = 0
        for num in sorted(counter):
            while counter.get(num, 0) and counter.get(num*2, 0):
                counter[num] -= 1
                counter[num*2] -= 1
        return not(any(counter.values()))

    def canReorderDoubled_best_speed(self, ls: List[int]) -> bool:
        counter = collections.Counter(ls)
        for v in sorted(counter.keys()):
            count = counter[v]
            if count == 0:
                continue
            if v < 0:
                if abs(v) % 2 == 1:
                    return False
                if counter[v] > counter[v // 2]:
                    return False
                counter[v // 2] -= counter[v]
            else:
                if counter[v] > counter[2 * v]:
                    return False
                counter[2 * v] -= counter[v]
            counter[v] = 0
        return sum(counter.values()) == 0

    def canReorderDoubled_1st_memory_2nd_best_speed(self, arr):
        c = Counter(arr)
        for x in sorted(c, key=abs):
            if c[x] > c[2 * x]:
                return False
            c[2 * x] -= c[x]
        return True
