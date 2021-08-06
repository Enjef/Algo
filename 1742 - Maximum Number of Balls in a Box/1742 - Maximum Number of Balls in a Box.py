class Solution:
    def countBalls(
            self,
            lowLimit: int,
            highLimit: int) -> int:  # 16.54% 81.14%
        boxes = {}
        for i in range(lowLimit, highLimit+1):
            b_sum = sum([int(x) for x in list(str(i))])
            if b_sum not in boxes:
                boxes[b_sum] = 0
            boxes[b_sum] += 1
        return max(boxes.values())

    def countBalls_best(self, lowLimit: int, highLimit: int) -> int:
        # Maximum 99999
        box = [0] * 46
        lo = lowLimit
        number = 0
        while lo > 0:
            number += lo % 10
            lo //= 10
        box[number] = 1
        for i in range(lowLimit + 1, highLimit + 1):
            j = i
            # Deal with trailing 0
            while j % 10 == 0:
                number -= 9
                j //= 10
            number += 1
            box[number] += 1
        return max(box)
