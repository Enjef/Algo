class Solution:
    def queensAttacktheKing(self, queens, king):  # 64.22% 15.20%
        queens = set(tuple(x) for x in queens)
        x, y = king
        out = []
        while x > -1 and y > -1:
            if (x, y) in queens:
                out.append((x, y))
                break
            x -= 1
            y -= 1
        x, y = king
        while x > -1:
            if (x, y) in queens:
                out.append((x, y))
                break
            x -= 1
        x, y = king
        while x > -1 and y < 8:
            if (x, y) in queens:
                out.append((x, y))
                break
            x -= 1
            y += 1
        x, y = king
        while y < 8:
            if (x, y) in queens:
                out.append((x, y))
                break
            y += 1
        x, y = king
        while x < 8 and y < 8:
            if (x, y) in queens:
                out.append((x, y))
                break
            x += 1
            y += 1
        x, y = king
        while x < 8:
            if (x, y) in queens:
                out.append((x, y))
                break
            x += 1
        x, y = king
        while x < 8 and y > -1:
            if (x, y) in queens:
                out.append((x, y))
                break
            x += 1
            y -= 1
        x, y = king
        while y > -1:
            if (x, y) in queens:
                out.append((x, y))
                break
            y -= 1
        return out

    def queensAttacktheKing_best_speed(
            self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        dirs = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, -1], [0, 1],
            [1, -1], [1, 0], [1, 1]
        ]
        lookup, res = {(i, j) for i, j in queens}, []
        for dx, dy in dirs:
            for i in range(8):
                x, y = king[0]+dx*i, king[1]+dy*i
                if not 0 <= x < 8 or not 0 <= y < 8:
                    break
                if (x, y) in lookup:
                    res.append([x, y])
                    break
        return res

    def queensAttacktheKing(self, queens, king):
        queen_set = {(i, j) for i, j in queens}
        res = []
        for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]:
            x, y = king[0], king[1]
            while 0 <= x < 8 and 0 <= y < 8:
                x += dx
                y += dy
                if (x, y) in queen_set:
                    res.append([x, y])
                    break
        return res
