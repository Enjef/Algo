class Solution:
    # 73.55% 80.82%
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        for row in matrix:
            for el in row:
                heappush(arr, el)
        while k-1:
            heappop(arr)
            k -= 1
        return heappop(arr)
