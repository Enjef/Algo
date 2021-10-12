class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:  # 34.39% 93.56%
        stones.sort()
        while len(stones) > 1:
            new = abs(stones.pop() - stones.pop())
            if new:
                stones.append(new)
                stones.sort()
        if not stones:
            return 0
        return stones[0]

    def lastStoneWeight_pop_max(
            self,
            stones: List[int]) -> int:  # 21.41% 77.95 %
        stones.sort()
        while len(stones) > 1:
            new = abs(
                stones.pop(stones.index(max(stones))) -
                stones.pop(stones.index(max(stones)))
            )
            if new:
                stones.append(new)
        if not stones:
            return 0
        return stones[0]

    def lastStoneWeight_best_memory(self, stones: List[int]) -> int:
        stones = sorted(stones)
        while len(stones) > 1:
            y = stones.pop(-1)
            x = stones.pop(-1)
            if x != y:
                stones.append(y-x)
                stones = sorted(stones)
        return stones[0] if len(stones) == 1 else 0
