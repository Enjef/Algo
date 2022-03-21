class Solution:
    def nextGreaterElement(self, n: int) -> int:  # 85.19% 85.19%
        if n < 10:
            return -1
        num = list(map(int, str(n)))
        size = len(num)
        i = size-2
        while i > 0 and num[i] >= num[i+1]:
            i -= 1
        if num[i] < num[i+1]:
            target = 10
            for el in num[i+1:]:
                if num[i] < el < target:
                    target = el
            j = i+num[i+1:].index(target)+1
            num[i], num[j] = num[j], num[i]
            num[i+1:] = sorted(num[i+1:])
        num = int(''.join(map(str, num)))
        return num if n < num < 2**31 else -1
