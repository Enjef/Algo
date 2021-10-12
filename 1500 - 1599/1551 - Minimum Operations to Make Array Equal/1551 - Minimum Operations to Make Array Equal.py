class Solution:
    def minOperations_my(self, n: int) -> int:  # 9,79%
        out = 0
        arr = []
        for i in range(n):
            arr.append(2 * i + 1)
        avrg = sum(arr) // n
        for i in arr:
            out += abs(avrg-i)
        return out // 2

    def minOperations(self, n: int) -> int:
        return sum([n - i for i in range(1, n, 2)])

    def minOperations_best(self, n: int) -> int:
        return n*n // 4
