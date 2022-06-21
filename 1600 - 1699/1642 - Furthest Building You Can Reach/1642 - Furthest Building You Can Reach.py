class Solution:
    #  28.05% 54.37%
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        way = []
        small = 0
        n = len(heights)
        for i in range(1, n):
            if heights[i-1] >= heights[i]:
                continue
            if ladders and len(way) < ladders:
                heappush(way, heights[i] - heights[i-1])
            else:
                if way and way[0] < (heights[i] - heights[i-1]):
                    small += heappop(way)
                    heappush(way, heights[i] - heights[i-1])
                else:
                    small += heights[i] - heights[i-1]
                if len(way) == ladders and small > bricks:
                    return i-1
        return n-1

    def furthestBuilding_best_speed(self, heights: List[int], bricks: int, ladders: int) -> int:
        gaps = []
        for i in range(len(heights)-1):
            gap = heights[i+1] - heights[i]
            if gap <= 0:
                continue
            if ladders > 0:
                ladders -= 1
                heapq.heappush(gaps, gap)
                continue
            if gaps and gaps[0] < gap:
                min_gap = heapq.heappop(gaps)
                if bricks >= min_gap:
                    bricks -= min_gap
                    heapq.heappush(gaps, gap)
                    continue
                else:
                    return i
            if gap <= bricks:
                bricks -= gap
            else:
                return i
        return i + 1

    def furthestBuilding_2nd_best_speed(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        heap = []
        for i in range(n-1):
            h = heights[i+1] - heights[i]
            if h > 0:
                heappush(heap, h)
                if len(heap) > ladders:
                    min_h = heappop(heap)
                    bricks -= min_h
                if bricks < 0:
                    return i
        return n - 1

    def furthestBuilding_best_memory(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        for i in range(n-1):
            heights[i] = max(heights[i+1] - heights[i], 0)
        ladder_heap = []
        for i in range(n-1):
            if not heights[i]:
                continue
            if ladders:
                heappush(ladder_heap, heights[i])
                ladders -= 1
            else:
                if ladder_heap and ladder_heap[0] < heights[i] and bricks >= ladder_heap[0]:
                    old_h = heappop(ladder_heap)
                    heappush(ladder_heap, heights[i])
                    bricks -= old_h
                elif heights[i] <= bricks:
                    bricks -= heights[i]
                else:
                    return i
        return n - 1
