class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        permutation = list(range(1, m+1))  # 48.37% 35.56%
        out = []
        for el in queries:
            el_index = permutation.index(el)
            permutation.remove(el)
            permutation = [el] + permutation
            out.append(el_index)
        return out

    def processQueries_best(self, queries: List[int], m: int) -> List[int]:
        P = []
        ans = []
        for i in range(m):
            P.append(i+1)
        for i in queries:
            index = P.index(i)
            ans.append(index)
            P.pop(index)
            P.insert(0, i)
        return ans
