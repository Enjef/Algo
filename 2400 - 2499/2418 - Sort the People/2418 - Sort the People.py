class Solution:
    # 28.55% 47.21%
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [x[0] for x in sorted(zip(names, heights), key=lambda x: x[1], reverse=True)]

    def sortPeople_best_speed(self, names: List[str], heights: List[int]) -> List[str]:
        data = list(zip(names, heights))
        sort = sorted(data, key=lambda tup: tup[1], reverse=True)
        name = list(zip(*sort))
        return list(name[0])

    def sortPeople_3d_best_speed(self, names: List[str], heights: List[int]) -> List[str]:
        return [n for _,n in sorted(zip(heights,names),reverse=True)]

    def sortPeople_best_memory(self, names: List[str], heights: List[int]) -> List[str]:
        l = heights.copy()
        l.sort(reverse=True)
        res = []
        for i in l:
            res.append(names[heights.index(i)])
        return res
