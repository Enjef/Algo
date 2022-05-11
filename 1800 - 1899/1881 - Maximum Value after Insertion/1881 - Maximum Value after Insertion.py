class Solution:
    def maxValue(self, n: str, x: int) -> str:  # 73.93% 78.83%
        if n[0] == '-':
            for i in range(1, len(n)):
                if n[i] > str(x):
                    n = n[:i] + str(x) + n[i:]
                    break
            else:
                n += str(x)
        else:
            for i in range(len(n)):
                if n[i] < str(x):
                    n = n[:i] + str(x) + n[i:]
                    break
            else:
                n += str(x)
        return n

    def maxValue_best_speed(self, n: str, x: int) -> str:
        digit = str(x)
        if n[0] == '-':
            for i, d in enumerate(n[1:]):
                if d > digit:
                    return f'{n[:i + 1]}{digit}{n[i + 1:]}'
        else:
            for i, d in enumerate(n):
                if d < digit:
                    return f'{n[:i]}{digit}{n[i:]}'
        return n + digit
