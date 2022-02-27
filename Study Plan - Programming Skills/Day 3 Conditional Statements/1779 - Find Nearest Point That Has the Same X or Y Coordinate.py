class Solution:
    def nearestValidPoint(self, x, y, points) -> int: # 32.48% 96.73%
        min_idx = -1
        min_dist = float('inf')
        for i, (xx, yy) in enumerate(points):
            if xx != x and yy != y:
                continue
            cur = abs(x-xx) + abs(y-yy)
            if cur < min_dist:
                min_dist = cur
                min_idx = i
        return min_idx
