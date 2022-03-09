class Solution:
    def canMeasureWater(
            self, jug1Capacity: int, jug2Capacity: int,
            targetCapacity: int) -> bool:  # 5.00% 19.41%
        stack = set([(0, 0)])
        seen = set()
        while stack:
            next_move = set()
            for first, second in stack:
                if (first, second) in seen:
                    continue
                seen.add((first, second))
                if targetCapacity in [first, second, first+second]:
                    return True
                if (first, 0) not in seen:
                    next_move.add((first, 0))
                if (0, second) not in seen:
                    next_move.add((0, second))
                if (jug1Capacity, second) not in seen:
                    next_move.add((jug1Capacity, second))
                if (first, jug2Capacity) not in seen:
                    next_move.add((first, jug2Capacity))
                first_to_second = max(0, second-(jug1Capacity-first))
                second_to_first = min(jug1Capacity, first+second)
                if (second_to_first, first_to_second) not in seen:
                    next_move.add((second_to_first, first_to_second))
                first_to_second = max(0, second-(jug2Capacity-first))
                second_to_first = min(jug2Capacity, first+second)
                if (second_to_first, first_to_second) not in seen:
                    next_move.add((second_to_first, first_to_second))
            stack = next_move
        return False

    def canMeasureWater_one_liner(self, jug1: int, jug2: int, target: int):
        return jug1 + jug2 >= target and target % math.gcd(jug1, jug2) == 0


    def canMeasureWater_best_speed(
            self, jug1Capacity: int,
            jug2Capacity: int, targetCapacity: int) -> bool:
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        if (
            jug1Capacity == targetCapacity or
            jug2Capacity == targetCapacity or
            (jug1Capacity + jug2Capacity) == targetCapacity):
                return True
        return targetCapacity % gcd(jug1Capacity, jug2Capacity) == 0

    def canMeasureWater_best_memory(self, x, y, z):
            gcd, r = max(x, y), min(x, y)
            while r: 
                gcd, r = r, gcd % r
            return z == 0 or x + y >= z and z % gcd == 0
