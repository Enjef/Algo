class Solution:
    def numTrees(self, n):  # 57.59% 75.54%
        map = {0: 1, 1: 1}
        for x in range(2, n+1):
            map[x] = sum([map[y]*map[x-y-1] for y in range(x)])
        return map[n]


    @cache
    def numTrees_best(self, n: int) -> int:
        return (
            1 if n < 2 else
            sum(self.numTrees(i) * self.numTrees(n+~i) for i in range(n))
        )
