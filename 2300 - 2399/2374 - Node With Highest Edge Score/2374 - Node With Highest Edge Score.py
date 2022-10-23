class Solution:
    # 16.24% 21.94% (7.63% 22.64%)
    def edgeScore(self, edges: List[int]) -> int:
        count = defaultdict(int)
        for i, val in enumerate(edges):
            count[val] += i
        arr = []
        for key, val in count.items():
            heappush(arr, (-val, key))
        return heappop(arr)[1]

    # 39.02% 55.14% (30.97% 57.22%)
    def edgeScore_v2(self, edges: List[int]) -> int:
        count = defaultdict(int)
        max_val = 0
        for i, val in enumerate(edges):
            count[val] += i
            max_val = max(max_val, count[val])
        return sorted([idx for idx in count if count[idx] == max_val])[0]


class Solution_best_speed:
    def edgeScore_1st(self, edges: List[int]) -> int:
        n = len(edges)
        scores = [0] * (n + 1)
        max_score = 0
        max_index = -1
        for i, edge in enumerate(edges):
            scores[edge] += i
        for i in range(n + 1):
            if scores[i] > max_score:
                max_score = scores[i]
                max_index = i
        return max_index


class Solution_best_memory:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        ans = [0] * n
        for i, val in enumerate(edges):
            ans[val] += i
        return ans.index(max(ans))
