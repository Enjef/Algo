class Solution:
    # 64.26% 67.87% (45.13% 23.47%)
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        prev = bottom
        res = 0
        if prev < special[0]:
            res = max(res, special[0] - prev)
        for floor in special:
            if floor > top:
                break
            res = max(res, floor - prev - 1)
            prev = floor
        if floor < top:
            res = max(res, top - floor)
        return res


class Solution_best_speed:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special = sorted(special)
        maximum = special[0] - bottom
        for s1, s2 in zip(special[:len(special)], special[1:]):
            if maximum < s2 - s1 - 1:
                maximum = s2 - s1 - 1
        if maximum < top - special[-1]:
            maximum = top - special[-1]
        return maximum

    def maxConsecutive_v2(self, bottom: int, top: int, special: List[int]) -> int:
        special = sorted(special)
        l = bottom
        res = -math.inf
        for i in range(len(special)):
            res = max(res, special[i] - l)
            l = special[i] + 1
        if l == top:
            return res
        return max(res, top - l + 1)


class Solution_best_memory:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        res = special[0] - bottom
        for i in range(1, len(special)):
            res = max(res, special[i] - special[i - 1] - 1)
        return max(res, top - special[-1])
