class Solution:
    def minTimeToVisitAllPoints(
            self,
            points: List[List[int]]) -> int:  # 99.45% 89.35%
        total = 0
        for i in range(1, len(points)):
            if points[i][0] == points[i-1][0]:
                total += abs(points[i][1] - points[i-1][1])
            elif points[i][1] == points[i-1][1]:
                total += abs(points[i][0] - points[i-1][0])
            else:
                total += max(
                    abs(points[i][1] - points[i-1][1]),
                    abs(points[i][0] - points[i-1][0])
                )
        return total

    def minTimeToVisitAllPoints_mock(
            self,
            points: List[List[int]]) -> int:  # 36.77% 68.17%
        prev = points[0]
        out = 0
        for i in range(1, len(points)):
            x0, y0 = prev
            x1, y1 = points[i]
            x = max(x0, x1) - min(x0, x1)
            y = max(y0, y1) - min(y0, y1)
            dia = min(x, y)
            rest = max(x, y) - min(x, y)
            out += dia + rest
            prev = points[i]
        return out

    def minTimeToVisitAllPoints_mock_refactored(
            self,
            points: List[List[int]]) -> int:  # 63.78% 96.82%
        out = 0
        for i in range(1, len(points)):
            x0, y0 = points[i-1]
            x1, y1 = points[i]
            x = abs(x0 - x1)
            y = abs(y0 - y1)
            if x0 == x1:
                out += y
            elif y0 == y1:
                out += x
            else:
                dia = min(x, y)
                rest = abs(x - y)
                out += dia + rest
        return out
