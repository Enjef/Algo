class Solution:
    def clumsy(self, n: int) -> int:  # 56.63% 37.35%
        arr = list(range(n, 0, -1))
        arr[0] *= -1
        sign = 0
        total = 0
        priority = 0
        for i, num in enumerate(arr):
            if sign == 0:
                if i < len(arr)-1:
                    priority += -num * arr[i+1]
                else:
                    total -= num
                sign += 1
            elif sign == 1:
                sign += 1
                continue
            elif sign == 2:
                total += int(priority / num)
                priority = 0
                sign += 1
            elif sign == 3:
                total += num
                sign = 0
        if priority:
            total += priority
        return total

    def clumsy_best_speed(self, n: int, bases=(0, 1, 2, 6, 7)) -> int:
        if n <= 4:
            return bases[n]
        if not (n & 3):
            return n + 1
        return n - 1 if (n & 3) == 3 else n + 2

    def clumsy_2nd_best_speed(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 6
        if n == 4:
            return 7
        if n == 5:
            return 7
        if n % 4 == 2:
            return n+2
        elif n % 4 == 0:
            return n+1
        elif n % 4 == 3:
            return n - 1
        else:
            return n+2

    def clumsy_6th_best_speed(self, N: int) -> int:
        return [0, 1, 2, 6, 7][N] if N < 5 else N + [1, 2, 2, - 1][N % 4]

    def clumsy_best_memory(self, n: int) -> int:
        result = 0
        first = True
        if n == 3:
            return 6
        if n == 2:
            return 2
        if n == 1:
            return 1
        if n == 0:
            return 0
        while n >= 4:
            cur_result = int(n * (n - 1) / (n - 2))
            result = result + cur_result + n - 3 if first else result - cur_result + n - 3
            first = False
            n = n - 4
        return result - self.clumsy_best_memory(n)
