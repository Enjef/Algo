class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        s_map = {}
        for i in range(len(mat)):
            count = mat[i].count(1)
            if count not in s_map:
                s_map[count] = []
            s_map[count].append(i)
        weakest = sorted(s_map.keys(), reverse=True)
        out = []
        while k:
            weak = weakest.pop()
            if len(s_map[weak]) < k:
                out.extend([s_map[weak]])
                k -= len(s_map[weak])
            else:
                out.extend([s_map[weak][:k]])
                k = 0
        return [x for arr in out for x in arr]

    def kWeakestRows_best(self, mat: List[List[int]], k: int) -> List[int]:
        result = [(sum(row), i) for i, row in enumerate(mat)]
        result.sort()
        return [idx for val, idx in result[:k]]
