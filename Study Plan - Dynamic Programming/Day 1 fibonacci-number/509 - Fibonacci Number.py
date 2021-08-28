class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        fib_l = [0, 1]
        if n < 2:
            return fib_l[n-1]
        while n > 2:
            fib_l = [fib_l[1], fib_l[0] + fib_l[1]]
            n -= 1
        return sum(fib_l)
