class Solution:
    # 90.94% 43.48% (56.67% 43.48%)
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        count = defaultdict(int)
        for key, val in items1:
            count[key] += val
        for key, val in items2:
            count[key] += val
        return [(key, count[key]) for key in sorted(count)]


class Solution_best_speed:
    def mergeSimilarItems_1st(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        def keyMethod(a):
            return a[0]

        d1 = dict(items1)
        for [i, v] in items2:
            d1[i] = d1.get(i, 0) + v
        ans = list(d1.items())
        ans.sort(key=keyMethod)
        return ans


class Solution_best_memory:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        ret = items1+items2
        ret.sort()
        i = 0
        while i < len(ret):
            j = i+1
            while j < len(ret):
                if ret[i][0] == ret[j][0]:
                    ret[i][1] = ret[i][1]+ret[j][1]
                    del ret[j]
                j = j+1
            i = i+1
        return ret
