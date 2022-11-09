class Solution:
    # 57.4% 56.31%
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort()
        n = len(stockPrices)
        if n < 2:
            return 0
        res = 0
        if len(stockPrices) > 2:
            (x1, y1), (x2, y2), (x3, y3) = stockPrices[0: 3]
            if not (y1 - y2) * (x1 - x3) == (y1 - y3) * (x1 - x2):
                res += 1
        if n > 2:
            for i in range(n-2):
                (x1, y1), (x2, y2), (x3, y3) = stockPrices[i: i+3]
                if (y1 - y2) * (x1 - x3) == (y1 - y3) * (x1 - x2):
                    continue
                res += 1
            if (y1 - y2) * (x1 - x3) == (y1 - y3) * (x1 - x2):
                res += 1
            return res
        else:
            return 1

    # 77.19% 64.81% (40.30% 6.31%)
    def minimumLines_v2(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort()
        n = len(stockPrices)
        if n < 3:
            return int(n == 2)
        (x1, y1), (x2, y2), (x3, y3) = stockPrices[:3]
        res = int((y1 - y2) * (x1 - x3) != (y1 - y3) * (x1 - x2))
        for i in range(n-2):
            (x1, y1), (x2, y2), (x3, y3) = stockPrices[i: i+3]
            if (y1 - y2) * (x1 - x3) == (y1 - y3) * (x1 - x2):
                continue
            res += 1
        if (y1 - y2) * (x1 - x3) == (y1 - y3) * (x1 - x2):
            res += 1
        return res


class Solution_best_speed:
    def minimumLines(self, A: List[List[int]]) -> int:
        n = len(A)
        res = n - 1
        A.sort()
        for i in range(1, n - 1):
            a, b, c = A[i-1], A[i], A[i+1]
            if (b[0] - a[0]) * (c[1] - b[1]) == (c[0] - b[0]) * (b[1] - a[1]):
                res -= 1
        return res


class Solution_best_memory:
    def minimumLines(self, stock: List[List[int]]) -> int:
        stock.sort()
        n = len(stock)
        line = 1
        if len(stock) == 1:
            return 0
        if len(stock) == 2:
            return 1
        for i in range(1, n-1):
            p1, p2, p3 = stock[i-1], stock[i], stock[i+1]
            if (p1[1]-p2[1])*(p2[0]-p3[0]) != (p2[1]-p3[1])*(p1[0]-p2[0]):
                line += 1
        return line
