class Solution:
    # 15.38% 23.08%
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        res = min(income, brackets[0][0]) * brackets[0][1]/100
        income -= min(income, brackets[0][0])
        for i in range(1, len(brackets)):
            if income == 0:
                break
            res += min(income, brackets[i][0] -
                       brackets[i-1][0]) * brackets[i][1]/100
            income -= min(income, brackets[i][0]-brackets[i-1][0])
        return res

    # 15.38% 53.85%
    def calculateTax_v2(self, brackets: List[List[int]], income: int) -> float:
        res = min(income, brackets[0][0]) * brackets[0][1]/100
        income -= min(income, brackets[0][0])
        for i in range(1, len(brackets)):
            res += min(income, brackets[i][0] -
                       brackets[i-1][0]) * brackets[i][1]/100
            income -= min(income, brackets[i][0]-brackets[i-1][0])
        return res

    # 15.38% 53.85%
    def calculateTax_v3(self, brackets: List[List[int]], income: int) -> float:
        return sum([(min(income, (cur-prev))*percent/100, income:=income-min(income, cur-prev))[0] for (prev, _), (cur, percent) in pairwise([(0, 0)]+brackets) if income > 0])

    # 23.08% 53.85%
    def calculateTax_v4(self, brackets: List[List[int]], income: int) -> float:
        return sum([(min(income, (cur-prev))*percent/100, income:=income-min(income, cur-prev))[0] for (prev, _), (cur, percent) in zip([(0, 0)]+brackets, brackets) if income > 0])

    # 15.38% 53.85%
    def calculateTax_v5(self, brackets: List[List[int]], income: int) -> float:
        return sum((min(income, (cur-prev))*percent/100, income:=income-min(income, cur-prev))[0] for (prev, _), (cur, percent) in zip([(0, 0)]+brackets, brackets) if income > 0)

    def calculateTax_best_speed(self, brackets: List[List[int]], income: int) -> float:
        ans = 0.000001
        last = 0
        for i in range(len(brackets)):
            threshold, rate = brackets[i]
            ans += rate/100 * (min(threshold, income) - last)
            last = threshold
            if income < threshold:
                break
        return ans

    def calculateTax_best_memory(self, brackets: List[List[int]], income: int) -> float:
        taxes = 0
        for cent in range(100 * income):
            for upper, percent in brackets:
                if cent < 100 * upper:
                    taxes += percent / 100
                    break
        return taxes / 100
