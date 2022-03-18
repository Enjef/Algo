class Solution:
    def kClosest(self, points, k):  # 91.94% 13.29%
        distances = defaultdict(list)
        for x, y in points:
            distances[(x*x+y*y)**0.5].append((x, y))
        out = []
        for key in sorted(distances):
            out.extend(distances[key])
            if len(out) >= k:
                break
        return out[:k]
