class Solution:
    def countPoints(self, points, queries):
        out = {i: 0 for i in range(1, len(queries) + 1)}
        for point in points:
            for i, circle in enumerate(queries):
                if (
                    (point[0] - circle[0]) ** 2 + (point[1] - circle[1]) ** 2
                        <= circle[2] * circle[2]):
                    out[i+1] += 1
        return list(out.values())
