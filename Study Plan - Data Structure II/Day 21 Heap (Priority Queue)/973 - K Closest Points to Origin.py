class Solution:
    def kClosest(
            self,
            points: List[List[int]],
            k: int) -> List[List[int]]:  # 86.53% 33.29%
        out = []
        for x, y in points:
            dist = (x*x + y*y)**0.5
            out.append((dist, (x, y)))
        out = [x[1] for x in sorted(out)]
        return out[:k]

    def kClosest_heap_mem(
            self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for i, point in enumerate(points):
            min_heap.append((sqrt(point[0]**2 + point[1]**2), i))
        heapq.heapify(min_heap)
        i = 0
        result = []
        while (i < k):
            popped = heapq.heappop(min_heap)
            result.append(points[popped[1]])
            i += 1
        return result

    def kClosest_heap_speed(
            self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = -(x*x + y*y)
            if len(heap) < k:
                heapq.heappush(heap, (dist, x, y))
            else:
                heapq.heappushpop(heap, (dist, x , y))
        return [[x,y] for (dist, x, y) in heap]
