class Solution:
    def fairCandySwap(
            self,
            aliceSizes: List[int],
            bobSizes: List[int]) -> List[int]:  # Time Limit Exceeded
        diff = sum(aliceSizes) - sum(bobSizes)
        for al in aliceSizes:
            for bo in bobSizes:
                if (
                        abs(al - bo) + abs(bo - al) == abs(diff) and
                        (al - bo)/abs(al - bo) == diff/abs(diff)):
                    return [al, bo]
        return

    def fairCandySwap_best_speed(
            self,
            aliceSizes: List[int],
            bobSizes: List[int]) -> List[int]:
        Sa, Sb = sum(aliceSizes), sum(bobSizes)
        setB = set(bobSizes)
        for x in aliceSizes:
            if x + (Sb - Sa) / 2 in setB:
                return [x, x + (Sb - Sa) / 2]

    def fairCandySwap_best_memory(
            self,
            aliceSizes: List[int],
            bobSizes: List[int]) -> List[int]:
        aliceSizes = sorted(aliceSizes)
        bobSizes = sorted(bobSizes)
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        swap = 0
        if sumB > sumA:
            sumA, sumB = sumB, sumA
            aliceSizes, bobSizes = bobSizes, aliceSizes
            swap = 1
        n = len(aliceSizes)
        m = len(bobSizes)
        i = n - 1
        while i >= 0:
            j = m - 1
            while aliceSizes[i] <= bobSizes[j] and j - 1 >= 0:
                j -= 1
            while j >= 0:
                if (
                        aliceSizes[i] > bobSizes[j] and
                        sumA - aliceSizes[i] + bobSizes[j] ==
                        sumB + aliceSizes[i] - bobSizes[j]):
                    return (
                            [aliceSizes[i], bobSizes[j]] if
                            not swap else [bobSizes[j], aliceSizes[i]]
                        )
                else:
                    j -= 1
            i -= 1
        return []
