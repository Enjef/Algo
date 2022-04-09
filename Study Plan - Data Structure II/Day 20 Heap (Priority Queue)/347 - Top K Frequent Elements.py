class Solution:
    def topKFrequent(
            self, nums: List[int], k: int) -> List[int]:  # 55.48% 84.54%
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        return sorted(count, key=count.get)[-k:]

    def topKFrequent_best_speed(self, nums: List[int], k: int) -> List[int]:
        d = collections.defaultdict(int)
        for num in nums:
            d[num] += 1
        h = []
        for key, val in d.items():
            if not h or len(h) < k:
                heapq.heappush(h, (val, key))
            else:
                if h[0][0] < val:
                    heapq.heappop(h)
                    heapq.heappush(h, (val, key))
        out = []
        for _ in range(k):
            curr = heapq.heappop(h)
            out.append(curr[1])
        return out

    def topKFrequent_3d_best_speed(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        heap = [(-v, k) for k, v in freq.items()]
        heapq.heapify(heap)
        output = []
        for i in range(k):
            v, k = heapq.heappop(heap)
            output.append(k)
        return output
