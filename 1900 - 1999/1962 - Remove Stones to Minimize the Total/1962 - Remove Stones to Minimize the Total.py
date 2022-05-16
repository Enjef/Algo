class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:  # 92.61% 22.51%
        piles = [-x for x in piles]
        heapify(piles)
        while k:
            k -= 1
            heappush(piles, heappop(piles)//2)
        return -sum(piles)

    def minStoneSum_best_speed(self, piles: List[int], k: int) -> int:
        piles = [-p for p in piles]
        heapify(piles)
        p = heappop(piles)
        for _ in range(k):
            p = heappushpop(piles, p + (-p) // 2)
        heappush(piles, p)
        return -sum(piles)

    def minStoneSum(self, piles: List[int], k: int) -> int:
        A = [-a for a in piles]
        heapq.heapify(A)
        for i in range(k):
            heapq.heapreplace(A, A[0] // 2)
        return -sum(A)

    def minStoneSum_best_memory(self, piles: List[int], k: int) -> int:
        piles = [x * -1 for x in piles]
        q.heapify(piles)
        while k > 0:
            val = floor((q.heappop(piles)) // 2)
            q.heappush(piles, val)
            k -= 1
        return int(abs(sum(piles)))
