class Solution:
    def isCovered(
        self, ranges: List[List[int]], left: int, right: int
    ) -> bool:
        target = list(range(left, right+1))
        for i in ranges:
            for j in range(i[0], i[1]+1):
                if j in target:
                    target.remove(j)
        return not target

    def isCovered_better(
        self, ranges: List[List[int]], left: int, right: int
    ) -> bool:
        for i in range(left, right + 1):
            for a, b in ranges:
                if a <= i <= b:
                    break
            else:
                return False
        return True
