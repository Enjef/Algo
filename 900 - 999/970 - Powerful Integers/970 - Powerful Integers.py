class Solution:
    def powerfulIntegers(
            self, x: int, y: int, bound: int) -> List[int]:  # 78.79% 30.30%
        if bound < 2:
            return []
        out = set()
        i = 0
        while True:
            cur = x**i
            if cur > bound or cur+1 in out and x == 1:
                break
            j = 0
            while True:
                total = cur + y**j
                if total > bound or total in out and y == 1:
                    break
                out.add(total)
                j += 1
            i += 1
        return out

    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if x > y:
            x, y = y, x
        if x == 1:
            if y == 1:
                return [2] if bound >= 2 else []
            else:
                bound -= 1
                yy = 1
                res = []
                while yy <= bound:
                    res.append(yy + 1)
                    yy *= y
                return res
        xx = 1
        res = set()
        while xx < bound:
            yy = 1
            while yy + xx <= bound:
                res.add(yy + xx)
                yy *= y
            xx *= x
        return list(res)

    def powerfulIntegers_best_memory(
            self, x: int, y: int, bound: int) -> List[int]:
        res = set()
        for i in range(int(10**6**0.2)):
            for j in range(int(10**6**0.2)):
                if x**i + y**j <= bound:
                    res.add(x**i + y**j)
                else:
                    break
        return list(res)
