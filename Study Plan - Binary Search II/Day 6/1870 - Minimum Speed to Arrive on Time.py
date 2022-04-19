class Solution:
    def minSpeedOnTime(self, dist, hour):  # 98.45% 49.22%
        left, right = 1, 10**7+1
        while left < right:
            mid = left + (right-left)//2
            cur = sum([ceil(point/mid) for point in dist[:-1]])+dist[-1]/mid
            if cur > hour:
                left = mid + 1
            else:
                right = mid
        return -1 if right == 10**7+1 else right
