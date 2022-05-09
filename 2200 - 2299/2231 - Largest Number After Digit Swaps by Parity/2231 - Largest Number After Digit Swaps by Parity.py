class Solution:
    def largestInteger(self, num: int) -> int:  # 97.11% 99.01%
        odd = []
        odd_idx = []
        even = []
        even_idx = []
        for i, el in enumerate(str(num)):
            if int(el) % 2:
                odd.append(el)
                odd_idx.append(i)
            else:
                even.append(el)
                even_idx.append(i)
        odd.sort(reverse=True)
        even.sort(reverse=True)
        out = [''] * (len(odd) + len(even))
        for i, idx in enumerate(odd_idx):
            out[idx] = odd[i]
        for i, idx in enumerate(even_idx):
            out[idx] = even[i]
        return ''.join(out)

    def largestInteger_best_speed(self, num: int) -> int:
        num = [char for char in str(num)]
        ret = []
        even, odd = [], []
        for char in num:
            if int(char) & 1:
                odd.append(char)
            else:
                even.append(char)
        even.sort(reverse=True)
        odd.sort(reverse=True)
        for char in num:
            if int(char) & 1:
                ret.append(odd.pop(0))
            else:
                ret.append(even.pop(0))
        return ''.join(ret)


class Solution_2nd_best_speed:
    def m(self, l1, l2):
        l1.sort(reverse=False)
        total = 0
        for i in range(len(l1)):
            total += l1[i] * pow(10, l2[i])
        return total
        
    def largestInteger(self, num: int) -> int:
        odd1 = []
        odd2 = []
        even1 = []
        even2 = []
        p = 0
        while num > 0:
            digit = num % 10
            if digit % 2 == 0:
                even1.append(digit)
                even2.append(p)
            else:
                odd1.append(digit)
                odd2.append(p)
            num = num // 10
            p += 1
        return self.m(odd1, odd2) + self.m(even1, even2)
