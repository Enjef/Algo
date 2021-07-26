class Solution(object):
    def countGoodRectangles(self, rectangles):  # 60.22% 39.23%
        squares = []
        for rectangle in rectangles:
            squares.append(min(rectangle[0], rectangle[1]))
        return squares.count(max(squares))

    def countGoodRectangles_best(self, rectangles):
        a = [min(x[0], x[1]) for x in rectangles]
        m = max(a)
        return a.count(m)