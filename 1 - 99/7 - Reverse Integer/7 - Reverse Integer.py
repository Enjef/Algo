class Solution:
    def reverse(self, x: int) -> int:  #  49.21% 74.40%
        if x < 0:
            x = -int(str(x)[:0:-1])
        else:
            x = int(str(x)[::-1])
        if -2**31 <= x <= 2**31 - 1:
            return x
        return 0

    def reverse_mock(self, x: int) -> int:  # 90.52% 46.28%
        if x < 0:
            x = int(''.join(['-', str(int(-1*x))[::-1]]))
        else:
            x = int(str(int(x))[::-1])
        return x if -2**31 <= x <= 2**31-1 else 0

    def reverse_best_speed(self, x: int) -> int:
        max_32 = 2**31 - 1
        if abs(x) > max_32:
            return 0
        if x < 0:
            reverse_int = -int(str(abs(x))[::-1])
        else:
            reverse_int = int(str(x)[::-1])
        if abs(reverse_int) > max_32:
            return 0
        else:
            return reverse_int

    def reverse_best_memory(self, x: int) -> int:
        result, x_remaining = 0, abs(x)
        while x_remaining:
            result = result * 10 + x_remaining % 10
            x_remaining //= 10
        if result > 2**31-1:
            return 0
        return -result if x < 0 else result
