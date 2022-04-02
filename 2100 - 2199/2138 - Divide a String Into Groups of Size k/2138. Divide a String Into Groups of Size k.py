class Solution:
    def divideString(self, s, k, fill):  # 80.19% 78.93%
        out = [s[i:i+k] for i in range(0, len(s), k)]
        if len(out[-1]) < k:
            out[-1] = ''.join([out[-1], fill*(k-len(out[-1]))])
        return out

    def divideString_best_speed(self, s: str, k: int, fill: str) -> List[str]:
        l = []
        if len(s) % k != 0:
            s += fill*(k-len(s) % k)
        for i in range(0, len(s), k):
            l.append(s[i:i+k])
        return l

    def divideString_memory_best(self, s: str, k: int, fill: str) -> List[str]:
        res = [s[i:i+k] for i in range(0, len(s), k)]
        res[-1] += fill*(k-len(res[-1]))
        return res
