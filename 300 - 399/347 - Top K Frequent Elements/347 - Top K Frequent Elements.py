class Solution:
    def topKFrequent(self, nums, k):  # 91.96% 68.16%
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        return sorted(count, key=count.get)[-k:]

    def topKFrequent_daily(self, nums, k):  # 27.80% 91.71%
        out = []
        heapify(out)
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        for key in counter:
            if len(out) < k:
                heappush(out, (counter[key], key))
            else:
                heappushpop(out, (counter[key], key))
        return [x[1] for x in out]

    def topKFrequent_best_speed(self, nums: List[int], k: int) -> List[int]:
        bucket = defaultdict(list)
        counter = Counter(nums)
        max_freq = -1
        for num, freq in counter.items():
            bucket[freq].append(num)
            max_freq = max(max_freq, freq)
        results = []
        start_freq = max_freq
        while len(results) < k:
            if start_freq in bucket:
                results.extend(bucket[start_freq])
            start_freq -= 1
        return results

    def topKFrequent_2nd_best_speed(self, nums: List[int], k: int) -> List[int]:
        import collections, heapq
        counter = collections.Counter(nums)
        pq = []
        nums = set(nums)
        for num in nums:
            cnt = counter[num]
            heapq.heappush(pq, (-cnt, num))
        ret = []
        for _ in range(k):
            ret.append(heapq.heappop(pq)[1])
        return ret

    def topKFrequent_3d_best_speed(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        keys = list(count.keys())
        if k >= len(keys):
            return keys
        return nlargest(k, keys, key=count.get)
