class ProductOfNumbers:  # 51.08% 11.90%
    def __init__(self):
        self.prod = [(1, float('inf'))]

    def add(self, num: int) -> None:
        if num == 0:
            self.prod.append((1, 0))
        else:
            self.prod.append((self.prod[-1][0]*num, self.prod[-1][1]+1))

    def getProduct(self, k: int) -> int:
        if self.prod[-1][1] <= k-1:
            return 0
        else:
            return self.prod[-1][0]//self.prod[-k-1][0]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)


class ProductOfNumbers_best_speed:
    def __init__(self):
        self.data = []
        self.product = 1

    def add(self, num: int) -> None:
        if num != 0:
            self.product *= num
            self.data.append(self.product)
        else:
            self.data = []
            self.product = 1

    def getProduct(self, k: int) -> int:
        if len(self.data) < k:
            return 0
        if len(self.data) == k:
            return self.data[-1]
        else:
            return int(self.data[-1] / self.data[-1-k])


class ProductOfNumbers_best_memory:
    def __init__(self):
        self.prod = [1]
        self.val = []

    def add(self, num: int) -> None:
        self.val.append(num)
        self.prod.append(self.prod[-1]*num)

    def getProduct(self, k: int) -> int:
        if self.prod[-1] == 0 and (k>len(self.val) or self.prod[-k-1]==0):
            val = 1
            for x in self.val[-k:]:
                val *= x
            return val
        else:
            return self.prod[-1] // self.prod[-k-1]
