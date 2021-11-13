class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:  # 78.04% 78.86%
        lineeqs = defaultdict(set)
        res = 0
        for i in range(len(points)):
            lineeqs = defaultdict(int)
            for j in range(i+1, len(points)):
                if points[i][1] == points[j][1]:
                    key = ("y", points[i][1])
                elif points[i][0] == points[j][0]:
                    key = ("x", points[i][0])
                else:
                    m = (points[i][1]-points[j][1])/(points[i][0]-points[j][0])
                    key = (m, -m*points[i][0]+points[i][1])
                lineeqs[key] += 1
                res = max(res, lineeqs[key])
        return res+1

    def maxPoints_dict(self, points: List[List[int]]) -> int:  # 85.70% 78.86%
        res = 0
        for i in range(len(points)):
            lines = {}
            for j in range(i+1, len(points)):
                if points[i][1] == points[j][1]:
                    key = ("y", points[i][1])
                elif points[i][0] == points[j][0]:
                    key = ("x", points[i][0])
                else:
                    m = (points[i][1]-points[j][1])/(points[i][0]-points[j][0])
                    key = (m, -m*points[i][0]+points[i][1])
                lines[key] = lines.get(key, 0) + 1
                res = max(res, lines[key])
        return res+1
