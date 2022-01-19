class Cashier:  # 23.87% 32.26%
    def __init__(self, n: int, discount: int, products, prices):
        self.n = n-1
        self.cur = 0
        self.discount = (100-discount)/100
        self.prices = dict(zip(products, prices))

    def getBill(self, product: List[int], amount: List[int]) -> float:
        total = 0
        for typ, amt in zip(product, amount):
            total += self.prices[typ] * amt
        if self.cur == self.n:
            self.cur = 0
            return total*self.discount
        self.cur += 1
        return total


class Cashier_best_speed:

    def __init__(self, n, discount, products, prices):
        self.products = dict(zip(products, prices))
        self.n = n
        self.discount = discount

        self.n_cust = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        bill = sum(self.products[p] * amt for p, amt in zip(product, amount))
        self.n_cust += 1
        if self.n_cust == self.n:
            self.n_cust = 0
            bill = self.addDiscount(bill, self.discount)
        return bill

    def addDiscount(self, bill, discount):
        return bill * ((100.0 - discount) / 100.0)


class Cashier_best_memory:
    def __init__(self, n, discount, products, prices):
        self.count = 0
        self.luck = n
        self.dis = (100-discount)/100
        self.prods = products
        self.price = prices

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.count += 1
        total = 0
        for i in range(len(product)):
            idx = self.prods.index(product[i])
            total += amount[i] * self.price[idx]
        if self.count % self.luck == 0:
            return (total*self.dis)
        return total
