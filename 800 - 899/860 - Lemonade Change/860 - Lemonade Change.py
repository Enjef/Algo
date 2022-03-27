class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:  # 55.73% 9.27%
        cashbox = {
            5: 0,
            10: 0,
            20: 0
        }

        for bill in bills:
            diff = bill - 5
            cashbox[bill] += 1
            while diff:
                if diff >= 10:
                    if cashbox[10]:
                        cashbox[10] -= 1
                        diff -= 10
                    elif cashbox[5]:
                        cashbox[5] -= 1
                        diff -= 5
                    else:
                        return False
                elif diff == 5:
                    if cashbox[5]:
                        cashbox[5] -= 1
                        diff -= 5
                    else:
                        return False
        return not diff

    def lemonadeChange_best_speed(self, bills: List[int]) -> bool:
        count = [0 for i in range(2)]

        for b in bills:
            if b == 5:
                count[0] += 1
            elif b == 10:
                if count[0] > 0:
                    count[0] -= 1
                    count[1] += 1
                else:
                    return False
            elif b == 20:
                if count[1] > 0 and count[0] > 0:
                    count[1] -= 1
                    count[0] -= 1
                elif count[1] == 0 and count[0] >= 3:
                    count[0] -= 3
                else:
                    return False
        return True
