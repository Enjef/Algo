class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:  # 98.06% 87.50%
        stack = []
        for seats, start, end in trips:
            stack.extend([(start, seats), (end, -seats)])
        stack.sort()
        cur = 0
        for _, val in stack:
            cur += val
            if cur > capacity:
                return False
        return True

    # 25.04% 12.97% (97.13% 12.97%)
    def carPooling_all_list(self, trips: List[List[int]], capacity: int) -> bool:
        return all([(capacity := capacity-seats) >= 0 for _, seats in sorted([x for seats, start, end in trips for x in [(start, seats), (end, -seats)]])])

    # 71.00% 42.31%
    def carPooling_with_all_generator(self, trips: List[List[int]], capacity: int) -> bool:
        return all((capacity:=capacity-seats) >= 0 for _, seats in sorted([x for seats, start, end in trips for x in [(start, seats), (end, -seats)]]))

    # 91.85% 87.50%
    def carPooling_any(self, trips: List[List[int]], capacity: int) -> bool:
        return not any([1 for _, seats in sorted([x for seats, start, end in trips for x in [(start, seats), (end, -seats)]]) if (capacity:=capacity-seats) < 0])

    def carPooling_best_speed(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        heap = []
        for trip in trips:
            riders, start, end = trip
            if heap:
                while heap and start >= heap[0][0]:
                    _end, in_car = heapq.heappop(heap)
                    capacity += in_car
            if riders > capacity:
                return False
            capacity -= riders
            heapq.heappush(heap, [end, riders])
        return True

    def carPooling_best_memory(self, trips: List[List[int]], capacity: int) -> bool:
        import collections
        count = collections.Counter()
        for trip in trips:
            test_dict = list(range(trip[1], trip[2]))
            test_dict = collections.Counter({k: trip[0] for k in test_dict})
            count = count + test_dict
        return count.most_common(1)[0][1] <= capacity
