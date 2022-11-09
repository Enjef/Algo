class Solution:
    # 29.51% 33.40% (18.65% 33.40%)
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        arr = []
        res = 0
        for i, cap in enumerate(capacity):
            rock = rocks[i]
            if cap == rock:
                res += 1
            else:
                heappush(arr, (cap-rock))
        while additionalRocks and arr:
            space = heappop(arr)
            additionalRocks -= space
            if additionalRocks < 0:
                break
            res += 1
        return res

    # 73.98% 48.98%
    def maximumBags_v2(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        arr = []
        res = 0
        for i, cap in enumerate(capacity):
            rock = rocks[i]
            if cap == rock:
                res += 1
            else:
                arr.append(cap-rock)
        arr.sort(reverse=True)
        while additionalRocks and arr:
            additionalRocks -= arr.pop()
            if additionalRocks < 0:
                break
            res += 1
        return res

    # 48.36% 33.40% (29.10% 33.40%)
    def maximumBags_v3(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        arr = []
        res = 0
        n = len(capacity)
        for i in range(n):
            diff = capacity[i] - rocks[i]
            if diff:
                arr.append(diff)
            else:
                res += 1
        arr.sort(reverse=True)
        while additionalRocks and arr:
            additionalRocks -= arr.pop()
            if additionalRocks < 0:
                break
            res += 1
        return res

    # 77.26% 48.98% (24.60% 48.98%)
    def maximumBags_v4(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        arr = []
        res = 0
        n = len(capacity)
        for i in range(n):
            diff = capacity[i] - rocks[i]
            if not not diff:
                arr.append(diff)
            else:
                res += 1
        arr.sort(reverse=True)
        while additionalRocks and arr:
            additionalRocks -= arr.pop()
            if additionalRocks < 0:
                break
            res += 1
        return res


class Solution_best_speed:
    def maximumBags_1st(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        l = len(rocks)
        remain = sorted([capacity[i]-rocks[i] for i in range(l)])
        start, end = 0, l-1
        s = list(accumulate(remain))
        while end >= start:
            mid = (start+end)//2
            if s[mid] < additionalRocks:
                start = mid+1
            elif s[mid] > additionalRocks:
                end = mid-1
            else:
                return mid+1
        return end+1

    def maximumBags_2nd(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        remaining_capacity = [cap - rock for cap, rock in zip(capacity, rocks)]
        remaining_capacity.sort()
        ans = 0
        for i in remaining_capacity:
            if i > additionalRocks:
                break
            ans += 1
            additionalRocks -= i
        return ans

    def maximumBags_3d(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        return len([1 for n in accumulate(sorted(c - r for c, r in zip(capacity, rocks))) if n <= additionalRocks])


class Solution_best_memory:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        capacity = sorted([c-r for c, r in zip(capacity, rocks)])
        num = 0
        for x in capacity:
            if x <= additionalRocks:
                num += 1
                additionalRocks -= x
            else:
                break
        return num
