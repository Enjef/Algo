class Solution:
    def checkStraightLine(self, coordinates):  # 88.21% 37.70%
        all_x, all_y = list(zip(*coordinates))
        if len(set(all_x)) == 1 or len(set(all_y)) == 1:
            return True
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        for x3, y3 in coordinates[2:]:
            if not x2-x1 or not y2-y1 or (x3-x1)/(x2-x1) != (y3-y1)/(y2-y1):
                return False
        return True
