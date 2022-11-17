class Solution:
    # 36.25% 26.26%
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        if bx1 < ax1:
            ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 = bx1, by1, bx2, by2, ax1, ay1, ax2, ay2
        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)
        if ax2 <= bx1 or ay1 >= by2 or ay2 <= by1:
            return area_a + area_b
        abx1 = max(ax1, bx1)
        aby1 = max(ay1, by1)
        abx2 = min(ax2, bx2)
        aby2 = min(ay2, by2)
        area_ab = (abx2 - abx1) * (aby2 - aby1)
        return area_a + area_b - area_ab


class Solution_best_speed:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        a = (ax2 - ax1) * (ay2 - ay1)
        b = (bx2 - bx1) * (by2 - by1)
        width = min(ax2, bx2) - max(ax1, bx1)
        height = min(ay2, by2) - max(ay1, by1)
        return a + b - max(height, 0) * max(width, 0)

    def computeArea_2nd(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)
        if bx1 < ax2 and bx2 > ax1 and by1 < ay2 and by2 > ay1:
            cx1 = max(ax1, bx1)
            cx2 = min(ax2, bx2)
            cy1 = max(ay1, by1)
            cy2 = min(ay2, by2)
            area_c = (cx2 - cx1) * (cy2 - cy1)
        else:
            area_c = 0
        area = area_a + area_b - area_c
        return area

    def computeArea_3d(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        overlap = max(min(C, G)-max(A, E), 0)*max(min(D, H)-max(B, F), 0)
        return (A-C)*(B-D) + (E-G)*(F-H) - overlap
