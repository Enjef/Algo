class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:  # 5.01% 5.15%
        temp = [[]]
        out = []
        for num in range(1, n+1):
            for item in temp[:]:
                cur = item + [num]
                if len(cur) == k:
                    out.append(cur)
                temp.append(cur)
        return out
