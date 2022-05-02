class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:  # 5.50% 60.24%
        if len(points) < 3:
            return False
        x1, y1, x2, y2, x3, y3 = (
            None, None, points[0][0], points[0][1], points[1][0], points[1][1])
        for xx, yy in points[2:]:
            x1, y1, x2, y2, x3, y3 = x2, y2, x3, y3, xx, yy
            triange_area = abs((0.5)*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
            if not triange_area:
                return False
        return True

    def isBoomerang_best_speed(self, points: List[List[int]]) -> bool:
        x0 = points[0][0]
        x1 = points[1][0]
        x2 = points[2][0]
        y0 = points[0][1]
        y1 = points[1][1]
        y2 = points[2][1]
        return (x0*y1 + x2*y0 + x1*y2 - x2*y1 - x0*y2 - x1*y0) != 0

    def isBoomerang_best_memory(self, p: List[List[int]]) -> bool:
        return (
            (p[0][0] - p[1][0]) * (p[0][1] - p[2][1]) !=
            (p[0][0] - p[2][0]) * (p[0][1] - p[1][1]))
