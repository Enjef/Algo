class Solution:
    # 52.66% 13.86%
    def lastStoneWeight(self, stones: List[int]) -> int:
        out = []
        for stone in stones:
            heappush(out, -stone)
        while len(out) > 1:
            heappush(out, heappop(out)-heappop(out))
        return -heappop(out)
