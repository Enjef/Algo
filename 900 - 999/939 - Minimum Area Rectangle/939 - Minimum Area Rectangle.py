class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int: # 17.22% 94.30%
        min_area = float('inf')
        n = len(points)
        points_dict = {}
        for x, y in points:
            if x not in points_dict:
                points_dict[x] = set()
            points_dict[x].add(y)
        for i in range(n):
            for j in range(i+1,n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2 or y1 == y2:
                    continue
                if y2 in points_dict[x1] and y1 in points_dict[x2]:
                    min_area = min(min_area, abs((x2-x1)*(y2-y1)))
        return min_area if min_area != float('inf') else 0

    def minAreaRect_best_speed(self, points: List[List[int]]) -> int:
        if len(points)<4:
            return 0
        xmapping = defaultdict(set)
        ymapping = defaultdict(set)
        for x,y in points:
            xmapping[x].add(y)
            ymapping[y].add(x)
        nx = len(xmapping)
        ny = len(ymapping)
        mapping  = xmapping if ny>nx else ymapping
        keys = sorted(list(mapping.keys()))
        area = float('inf')
        for i,x0 in enumerate(keys):
            for x1 in reversed(keys[:i]):
                if x0-x1>area:
                    break
                yset0,yset1 = mapping[x0],mapping[x1]
                interset =  sorted(yset0.intersection(yset1))
                if len(interset)>1:
                    min_ydiff = float("inf")
                    for j in range(len(interset)-1):
                        min_ydiff = min(min_ydiff,(interset[j+1]-interset[j]))
                    area = min(area,min_ydiff*(x0-x1))
        return 0 if area==float('inf') else area

    def minAreaRect_best_memory(self, points: List[List[int]]) -> int:
        points.sort()
        points_set = set([tuple(point) for point in points])
        smallest = float('inf')
        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points[i:], i):
                if (x1 < x2 and y1 < y2 and (x1, y2) in points_set and(x2, y1) in points_set):
                    area = (x2 - x1) * (y2 - y1)
                    smallest = min(smallest, area)
        return smallest if smallest != float('inf') else 0
