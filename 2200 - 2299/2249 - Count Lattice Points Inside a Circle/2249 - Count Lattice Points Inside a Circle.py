class Solution:
    # 5.43% 31.36% (TLE)
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        def inside(x, y, x_center, y_center, r):
            return (x - x_center) ** 2 + (y - y_center) ** 2 <= r ** 2

        good = set()
        for i, j, r in circles:
            for ii in range(i-r, i+r+1):
                for jj in range(j-r, j+r+1):
                    if inside(ii, jj, i, j, r):
                        good.add((ii, jj))
        return len(good)

    # 6.37% 31.36%
    def countLatticePoints_v2(self, circles: List[List[int]]) -> int:
        good = set()
        for i, j, r in circles:
            for ii in range(max(0, i-r), min(201, i+r+1)):
                for jj in range(max(0, j-r), min(201, j+r+1)):
                    if (ii - i) ** 2 + (jj - j) ** 2 <= r*r:
                        good.add((ii, jj))
        return len(good)

    # 89.09% 31.36% (82.27% 31.36%)
    def countLatticePoints_v3(self, circles: List[List[int]]) -> int:
        good = set()
        for i, j, r in {(i, j, r) for i, j, r in circles}: # lots of duplicates
            for ii in range(max(0, i-r), min(201, i+r+1)):
                for jj in range(max(0, j-r), min(201, j+r+1)):
                    if (ii - i) ** 2 + (jj - j) ** 2 <= r*r:
                        good.add((ii, jj))
        return len(good)

    # 89.09% 77.73% (85.91% 31.36%)
    def countLatticePoints_v4(self, circles: List[List[int]]) -> int:
        good = set()
        new = dict()
        for i, j, r in circles:
            cur = (i, j)
            if cur not in new:
                new[cur] = r
            new[cur] = max(new[cur], r)

        for (i, j), r in new.items():
            for ii in range(max(0, i-r), min(201, i+r+1)):
                for jj in range(max(0, j-r), min(201, j+r+1)):
                    if (ii - i) ** 2 + (jj - j) ** 2 <= r*r:
                        good.add((ii, jj))
        return len(good)

class Solution_best_speed:
    def countLatticePoints(self, c: List[List[int]]) -> int:
        ans, m = 0, [0]*40401
        c = set(((x, y, r) for x, y, r in c))
        for x, y, r in c:
            for i in range(x-r, x+r+1):
                d = int(sqrt(r*r-(x-i)*(x-i)))
                m[i*201+y-d:i*201+y+d+1] = [1]*(d+d+1)
        return sum(m)


class Solution_best_memory:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        ans = 0
        for x in range(201):
            for y in range(201):
                for cx, cy, r in circles:
                    if (x - cx) * (x - cx) + (y - cy) * (y - cy) <= r * r:
                        ans += 1
                        break
        return ans

    def countLatticePoints_2nd(self, circles: List[List[int]]) -> int:
        count = 0
        for x in range(min(triple[0]-triple[2] for triple in circles), max(triple[0]+triple[2] for triple in circles)+1):
            for y in range(min(triple[1]-triple[2] for triple in circles), max(triple[1]+triple[2] for triple in circles)+1):
                for circle in circles:
                    if (x-circle[0]) ** 2 + (y-circle[1]) ** 2 <= circle[2] ** 2:
                        count += 1
                        break
        return count
