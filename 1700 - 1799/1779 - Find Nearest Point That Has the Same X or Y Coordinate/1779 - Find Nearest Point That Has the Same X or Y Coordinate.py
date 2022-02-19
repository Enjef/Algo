class Solution:
    def nearestValidPoint(self, x: int, y: int, points) -> int: # 12.93% 99.52%
        res = -1
        dist = float('inf')
        for i, coord in enumerate(points):
            xx, yy = coord
            if not(x==xx or y==yy):
                continue
            cur = abs(x-xx)+abs(y-yy)
            if cur < dist:
                dist = cur
                res = i
        return res

    def nearestValidPoint_best_speed(self, x: int, y: int, points) -> int:
        h = []
        heapq.heapify(h)
        for index, point in enumerate(points):
            curr_x, curr_y = point
            if curr_x != x and curr_y != y:
                continue
            md = abs(x-curr_x) + abs(y-curr_y)
            heapq.heappush(h, (md, index))
        if h:
            return heapq.heappop(h)[1]
        else:
            return -1

    def nearestValidPoint_2nd_best_speed(self, x: int, y: int, points) -> int:
        validDists = {}
        for i, point in enumerate(points): 
            if point[0] == x or point[1] == y: 
                validDists[i] = abs(point[0] - x) + abs(point[1] - y)
        return min(validDists, key=validDists.get, default=-1)     

    def nearestValidPoint_best_memory(self, x: int, y: int, points) -> int:
        mindis = sys.maxsize
        minindex = len(points)
        for i in range(len(points)):
            p = points[i]
            dis = 0
            if p[0]  == x:
                dis = abs(p[1] - y)
            elif p[1] == y:
                dis = abs(p[0]-x)
            else:
                dis = sys.maxsize 
            if dis < mindis:
                mindis = min(dis,mindis)
                minindex = i
        return minindex if minindex < len(points) else -1 
