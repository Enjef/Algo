class Solution:
    def numWaterBottles(
            self,
            numBottles: int,
            numExchange: int) -> int:  # 77.15% 43.87%
        count = numBottles
        while numBottles >= numExchange:
            count += numBottles // numExchange
            numBottles = numBottles // numExchange + numBottles % numExchange
        return count

    def numWaterBottles_best_speed(
            self,
            numBottles: int,
            numExchange: int) -> int:
        full = numBottles
        empty = 0
        drunk = 0
        while (full > 0 or empty > numExchange):
            drunk += full
            empty += full
            full = empty // numExchange
            empty = empty % numExchange
        return drunk

    def numWaterBottles_best_memory(
            self,
            numBottles: int,
            numExchange: int) -> int:
        bottle = numBottles
        answer = numBottles
        while bottle >= numExchange:
            i, j = divmod(bottle, numExchange)
            bottle = i + j
            answer += i
        return answer
