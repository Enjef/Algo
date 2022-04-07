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

    def lastStoneWeight_heap(self, stones: List[int]) -> int:  # 78.86% 17.07%
        out = []
        heapify(out)
        for stone in stones:
            heappush(out, -stone)
        while len(out) >1:
            heappush(out, heappop(out)-heappop(out))
        return -heappop(out)

    def lastStoneWeight_best_speed(self, stones: List[int]) -> int:
        h = [-elem for elem in stones]
        heapq.heapify(h)
        while len(h) > 1:
            a, b = heapq.heappop(h), heapq.heappop(h)
            heapq.heappush(h, -abs(a - b))
        return abs(h[0])

    def lastStoneWeight_best_memory_old(self, stones: List[int]) -> int:
        stones = sorted(stones)
        while len(stones) > 1:
            y = stones.pop(-1)
            x = stones.pop(-1)
            if x != y:
                stones.append(y-x)
                stones = sorted(stones)
        return stones[0] if len(stones) == 1 else 0

    def lastStoneWeight_best_memory(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            z = abs(x - y)
            if z != 0:
                heapq.heappush(stones, z * -1)
        if len(stones) == 1:
            return stones[0] * -1
        else:
            return 0
