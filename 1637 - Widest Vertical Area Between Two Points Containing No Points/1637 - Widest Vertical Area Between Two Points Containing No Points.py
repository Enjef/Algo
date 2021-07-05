class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:  # 65.95%
        x_set = set()
        for point in points:
            x_set.add(point[0])
        x_set = sorted(list(x_set))
        x_max = 0
        for i in range(1, len(x_set)):
            x_max = max(x_max, x_set[i]-x_set[i-1])
        return x_max

    def maxWidthOfVerticalArea_s_best(self, points: List[List[int]]) -> int:
        li = sorted(x for x, y in points)
        maxi = 0
        for i in range(len(li)-1):
            if maxi < (li[i+1]-li[i]):
                maxi = li[i+1]-li[i]
        return maxi
