class Solution:
    def buildArray(
            self,
            target: List[int],
            n: int) -> List[str]:  # 71.63% 18.41%
        arr = []
        out = []
        for i in range(1, n+1):
            arr.append(i)
            out.append('Push')
            if arr[-1] not in target:
                arr.pop()
                out.append('Pop')
            if arr == target:
                break
        return out

    def buildArray_best(self, target: List[int], n: int) -> List[str]:
        res = []
        ptr = 0
        for i in range(1, n+1):
            if ptr == len(target):
                break
            if i != target[ptr]:
                res.append('Push')
                res.append('Pop')
            else:
                res.append('Push')
                ptr += 1
        return res
