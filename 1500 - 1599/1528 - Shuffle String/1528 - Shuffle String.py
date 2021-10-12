class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:  # 30%
        res = [''] * len(s)
        for i in range(len(res)):
            res[i] = s[indices.index(i)]
        return ''.join(res)

    def restoreString_best(self, s: str, indices: List[int]) -> str:  # best
        result = [""] * len(s)
        for i, letter in enumerate(s):
            result[indices[i]] = letter
        return "".join(result)
