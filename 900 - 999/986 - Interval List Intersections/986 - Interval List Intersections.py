class Solution:
    def intervalIntersection(
            self,
            firstList: List[List[int]],
            secondList: List[List[int]]) -> List[List[int]]:  # 26.95% 78.40%
        if not firstList or not secondList:
            return []
        i = 0
        j = 0
        out = []
        while i < len(firstList) and j < len(secondList):
            first_left, first_right = firstList[i]
            second_left, second_right = secondList[j]
            if first_left <= second_right and second_left <= first_right:
                out.append(
                    [
                        max(first_left, second_left),
                        min(first_right, second_right)
                    ]
                )
            if (
                    first_right < second_left or
                    (out and out[-1][1] == first_right)):
                i += 1
            elif (
                    second_right < first_left or
                    (out and out[-1][1] == second_right)):
                j += 1
            else:
                i += 1
                j += 1
        return out

    def intervalIntersection_best_speed(
            self,
            firstList: List[List[int]],
            secondList: List[List[int]]) -> List[List[int]]:
        fLen = len(firstList)
        sLen = len(secondList)
        f = s = 0
        res = []
        while f < fLen and s < sLen:
            if firstList[f][1] < secondList[s][0]:
                f += 1
                continue
            if secondList[s][1] < firstList[f][0]:
                s += 1
                continue
            res.append(
                [
                    max(firstList[f][0], secondList[s][0]),
                    min(firstList[f][1], secondList[s][1])
                ]
            )
            if firstList[f][1] < secondList[s][1]:
                f += 1
            else:
                s += 1
        return res


