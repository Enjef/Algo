class Solution:
    def findComplement(self, num: int) -> int:  # 52.34% 6.20%
        return int(''.join('1' if x == '0' else '0' for x in bin(num)[2:]), 2)

    def findComplement_best_speed(self, num: int) -> int:
        no = str(bin(num)[2:])
        ar = list(map(int, str(no)))
        for i in range(0, len(ar)):
            if ar[i] == 0:
                ar[i] = 1
            else:
                ar[i] = 0
        s = [str(i) for i in ar]
        res = "".join(s)
        return int(res, 2)

    def findComplement_best_memory(self, num: int) -> int:
        cur, bit = num, 1
        while cur:
            num = num ^ bit
            bit = bit << 1
            cur = cur >> 1
        return num
