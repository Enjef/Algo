class Solution:
    def frequencySort(self, s: str) -> str:  # 64.06% 44.88%
        counter = {}
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        chars = sorted(counter, key=counter.get, reverse=True)
        return ''.join([char*counter[char] for char in chars])

    def frequencySort_heap(self, s: str) -> str:
        res = ""
        dic = Counter(s)
        max_heap = [(-val, key) for key, val in dic.items()]
        heapq.heapify(max_heap)
        while max_heap:
            val, key = heapq.heappop(max_heap)
            res += key * (-val)
        return res   
