from bisect import bisect_right, bisect_left


class Solution:
    # 40.00% 5.00% ()
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        visits = defaultdict(int)
        events = []
        for start, end in flowers:
            events.extend([(start, 1), (end+1, -1)])
        events.extend([(x, 0) for x in persons])
        events.sort()
        cur = 0
        for time, event in events:
            cur += event
            visits[time] = cur
        return [visits[x] for x in persons]

    # 22.00% 55.50% (87.00% 65.50%)
    def fullBloomFlowers_v2(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        visits = dict((x, 0) for x in persons)
        events = []
        for start, end in flowers:
            events.extend([(start, 1), (end+1, -1)])
        events.extend([(x, 0) for x in persons])
        events.sort()
        cur = 0
        for time, event in events:
            cur += event
            if time in visits:
                visits[time] = cur
        return [visits[x] for x in persons]


class Solution_best_speed:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        sorted_starts = sorted(start for start, end in flowers)
        sorted_ends = sorted(end for start, end in flowers)
        num_flowers_in_bloom = [0] * len(persons)
        for idx, person in enumerate(persons):
            num_flowers_in_bloom[idx] = bisect_right(
                sorted_starts, person) - bisect_left(sorted_ends, person)
        return num_flowers_in_bloom

    def fullBloomFlowers_2nd(self, f: List[List[int]], p: List[int]) -> List[int]:
        s, e = sorted(a for a, b in f), sorted(b for a, b in f)
        return [bisect.bisect_right(s, i)-bisect.bisect_left(e, i) for i in p]

    def fullBloomFlowers_4th(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        flowers.sort()
        res = {}
        minHeap = []
        i = 0
        for p in sorted(persons):
            while i < len(flowers) and flowers[i][0] <= p:
                heappush(minHeap, flowers[i][1])
                i += 1
            while minHeap and minHeap[0] < p:
                heappop(minHeap)
            res[p] = len(minHeap)
        return [res[p] for p in persons]


class Solution_best_memory:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        p = [(arrival, index) for index, arrival in enumerate(persons)]
        p.sort()
        flowers.sort(reverse=True)
        results = [0] * len(p)
        heap = []
        for arrival, index in p:
            while len(flowers) > 0 and flowers[-1][0] <= arrival:
                start, end = flowers.pop()
                heappush(heap, end)
            while len(heap) > 0 and heap[0] < arrival:
                end = heappop(heap)
            results[index] = len(heap)
        return results
