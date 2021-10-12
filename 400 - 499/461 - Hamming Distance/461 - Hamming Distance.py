class Solution:
    def hammingDistance(self, x: int, y: int) -> int:  # 58.70% 11.53%
        x_bin = [int(x) for x in bin(x)[2:]]
        y_bin = [int(y) for y in bin(y)[2:]]
        count = 0
        if len(x_bin) < len(y_bin):
            x_bin = [0] * (len(y_bin) - len(x_bin)) + x_bin
        if len(x_bin) > len(y_bin):
            y_bin = [0] * (len(x_bin) - len(y_bin)) + y_bin
        for i in range(len(x_bin)):
            if x_bin[i] ^ y_bin[i] == 1:
                count += 1
        return count

    def hammingDistance_best(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")
