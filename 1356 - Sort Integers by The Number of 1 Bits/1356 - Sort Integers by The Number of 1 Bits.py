class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:  # 94.21% 72.86%
        return [x[1] for x in sorted([(bin(x).count('1'), x) for x in arr])]

    def sortByBits_best(self, arr: List[int]) -> List[int]:
        arr.sort()
        arr.sort(key=lambda x:bin(x).count('1'))
        return arr

    def sortByBits_second_to_best(self, arr: List[int]) -> List[int]:
        res = []
        for i in range(17):
            # max number of 16 bits
            res.append([])
        for i in arr:
            val = bin(i).count("1")
            res[val].append(i)
        ans = []
        for i in res:
            if len(i) > 0:
                if len(i) >= 1:
                    i.sort()
                ans = ans + i
        return ans
