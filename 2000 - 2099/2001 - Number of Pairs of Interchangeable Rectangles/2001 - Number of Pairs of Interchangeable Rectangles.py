class Solution:
    # 79.03% 51.31%
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        d = defaultdict(int)
        for width, height in rectangles:
            d[width/height] += 1
        return sum(comb(x, 2) for x in d.values() if x > 1)

    def interchangeableRectangles_v2(self, rectangles: List[List[int]]) -> int:  # 7.12% 19.85% (95.51% 41.57%)
        return sum([comb(x, 2) for x in Counter([width/height for width, height in rectangles]).values() if x > 1])

    def interchangeableRectangles_from_discussion(self, rectangles: List[List[int]]) -> int:
        return sum([x*(x-1)//2 for x in Counter([width/height for width, height in rectangles]).values()])
