class Solution:
    def findLeastNumOfUniqueInts(
            self, arr: List[int], k: int) -> int:  # 82.18% 71.94%
        counter = defaultdict(int)
        for num in arr:
            counter[num] += 1
        min_keys = sorted(counter, key=counter.get, reverse=True)
        while k > 0 and min_keys:
            k -= counter[min_keys.pop()]
        return len(min_keys) if k == 0 else len(min_keys) + 1

    def findLeastNumOfUniqueInts_v2(
            self, arr: List[int], k: int) -> int:  # 66.86% 71.94%
        counter = defaultdict(int)
        for num in arr:
            counter[num] += 1
        min_keys = sorted(counter, key=counter.get, reverse=True)
        n = len(min_keys)
        for i in range(n):
            cur = counter[min_keys.pop()]
            k -= cur
            if k <= 0:
                break
        return n-i-1 if k == 0 else n-i

    def findLeastNumOfUniqueInts_best_speed(self, arr, k):
        count = Counter(arr)
        ans = len(count)
        for i in sorted(count.values()):
            k -= i
            if k < 0:
                break
            ans -= 1
        return ans

    def findLeastNumOfUniqueInts_2nd_best_speed(self, arr, k):
        c = Counter(arr)
        cnt, remaining = Counter(c.values()), len(c)
        for key in range(1, len(arr) + 1):
            if k >= key * cnt[key]:
                k -= key * cnt[key]
                remaining -= cnt[key]
            else:
                return remaining - k // key
        return remaining

    def findLeastNumOfUniqueInts_best_memory(self, arr, k):
        if len(arr) == 1:
            if k > 0:
                return 0
            else:
                return 1
        arr = sorted(arr)
        heap = []
        currFreq = 1
        for i in range(1, len(arr)):
            if arr[i] != arr[i-1]:
                heapq.heappush(heap, (currFreq, arr[i-1]))
                currFreq = 0
            currFreq += 1
            if i == len(arr)-1:
                heapq.heappush(heap, (currFreq, arr[i]))
        while k > 0:
            freq, num = heapq.heappop(heap)
            if freq - 1 != 0:
                heapq.heappush(heap, (freq-1, num))
            k -= 1
        return len(heap)

    def findLeastNumOfUniqueInts_2nd_memory(self, arr, k):
        count = collections.Counter(arr)
        least_count = sorted(count.values())
        ans = len(count)
        for i in least_count:
            if k < i:
                return ans
            else:
                k -= i
                ans -= 1
        return 0
