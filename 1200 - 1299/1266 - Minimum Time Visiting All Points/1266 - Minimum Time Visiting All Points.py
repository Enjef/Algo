class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
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
