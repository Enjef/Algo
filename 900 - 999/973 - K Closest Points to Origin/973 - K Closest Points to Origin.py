class Solution:
    def kClosest(
            self,
            points: List[List[int]],
            k: int) -> List[List[int]]:  # 86.39% 33.08%
        out = []
        for x, y in points:
            dist = (x*x + y*y)**0.5
            out.append((dist, (x, y)))
        out = [x[1] for x in sorted(out)]
        return out[:k]

    def kClosest_best_speed(
            self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p: p[0]*p[0] + p[1]*p[1])
        return points[:k]
