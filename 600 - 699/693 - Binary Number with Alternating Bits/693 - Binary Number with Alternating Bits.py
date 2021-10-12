class Solution:
    def hasAlternatingBits(self, n: int) -> bool:  # 81.91% 36.19%
        n_str = str(bin(n))[2:]
        for i, el in enumerate(n_str):
            if i % 2 == 0 and el != '1' or i % 2 != 0 and el != '0':
                return False
        return True

    def hasAlternatingBits_refactored(self, n: int) -> bool:  # 94.67% 89.50%
        n_str = str(bin(n))[2:]
        for i in range(1, len(n_str)):
            if n_str[i] == n_str[i-1]:
                return False
        return True

    def hasAlternatingBits_best_speed(self, n: int) -> bool:
        binary_string = str(bin(n))
        alternating = True
        for i in range(len(binary_string) - 1):
            if binary_string[i] == binary_string[i + 1]:
                alternating = False
                break
        return alternating
