class Solution:
    def isRectangleOverlap(
            self, rec1: List[int], rec2: List[int]) -> bool:  # 84.39% 91.73%
        return (
            max(rec1[0], rec2[0]) < min(rec1[2], rec2[2]) and
            max(rec1[1], rec2[1]) < min(rec1[3], rec2[3])
        )

    def isRectangleOverlap_best_memory(
            self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        return not (x2 <= x3 or x1 >= x4 or y2 <= y3 or y1 >= y4)
