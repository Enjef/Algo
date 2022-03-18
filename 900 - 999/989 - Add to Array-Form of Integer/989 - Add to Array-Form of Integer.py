class Solution:
    def addToArrayForm(self, num, k):  # 55.43% 37.80%
        cur = 0
        for el in num:
            cur = cur*10 + el
        return [int(x) for x in str(cur+k)]

    def addToArrayForm_v2(self, num, k):  # 28.93% 94.47%
        cur = 0
        for el in num:
            cur = cur*10 + el
        return list(str(cur+k))

    def addToArrayForm_best_speed(self, num: List[int], k: int) -> List[int]:
        idx = len(num) - 1
        while k and idx > -1:
            curr = num[idx] + k
            k = curr // 10
            num[idx] = curr % 10
            idx -= 1
        if k:
            num = list(map(int, str(k))) + num
        return num

    def addToArrayForm_second_best_speed(self, num, k):
        n = len(num)
        i = n-1
        while k > 0 and i >= 0:
            num[i] += k
            k = num[i] // 10
            num[i] %= 10
            i -= 1
        if k > 0:
            rev_rest = []
            while k:
                rev_rest.append(k % 10)
                k //= 10
            num = rev_rest[::-1] + num
        return num

    def addToArrayForm_best_memory(self, num: List[int], k: int) -> List[int]:
        s = 0
        for i in num:
            s = s*10 + i
        s += k
        return str(s)
