class Solution:
    def removeDigit(self, number: str, digit: str) -> str:  # 38.93% 16.09%
        idx = None
        for i, char in enumerate(number):
            if char == digit:
                idx = i
            elif idx is not None and idx == i-1 and char > digit:
                return number[:idx] + number[idx+1:]
        return number[:idx] + number[idx+1:]

    def removeDigit_best_speed(self, n: str, d: str) -> str:
        res = ''
        for i in range(len(n)):
            if n[i] == d:
                if res == '':
                    res = n[:i] + n[i+1:]
                elif res < n[:i] + n[i+1:]:
                    res = n[:i] + n[i+1:]
        return res

    def removeDigit_best_memory(self, number: str, digit: str) -> str:
        largest = ''
        for i in range(len(number)):
            if number[i] == digit and number[:i] + number[i+1:] > largest:
                largest = number[:i] + number[i+1:]
        return largest
