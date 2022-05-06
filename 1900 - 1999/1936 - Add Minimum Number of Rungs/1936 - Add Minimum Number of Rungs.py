class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:  # 29.02% 35.75%
        cur = 0
        out = 0
        for rung in rungs:
            if (cur + dist) < rung:
                out += (rung - cur-1) // dist
            cur = rung
        return out

    def addRungs_best_speed(self, rungs: List[int], dist: int) -> int:
        res = int(0)
        cur_location = int(0)
        for rung in rungs:
            diff = (rung - cur_location)
            if diff > dist:
                division = diff / dist
                int_division = int(division)
                if division == int_division:
                    res = res + int_division - 1
                else:
                    res = res + int_division
            cur_location = rung
        return res

    def addRungs_2nd_best_speed(self, rungs: List[int], dist: int) -> int:
        prev, min_rungs = 0, 0
        for current in rungs:
            min_rungs += (current - prev - 1)//dist
            prev = current
        return min_rungs
