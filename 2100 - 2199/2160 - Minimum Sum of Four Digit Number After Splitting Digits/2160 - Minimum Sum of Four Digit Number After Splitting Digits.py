class Solution:
    def minimumSum(self, num: int) -> int:  # 20.98% 64.50%
        arr = sorted(str(num))
        return int(arr[0]+arr[2]) + int(arr[1]+arr[3])

    def minimumSum_best_speed(self, num: int) -> int:
        digit = []
        for i in range(1, 5):
            temp = num % 10
            digit.append(temp)
            num -= temp
            num = num // 10
        digit.sort()
        res = (digit[0] + digit[1]) * 10 + digit[2] + digit[3]
        return res
