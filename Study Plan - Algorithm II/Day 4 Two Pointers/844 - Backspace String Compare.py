class Solution:
    def backspaceCompare_pop(self, s: str, t: str) -> bool:  # 88.12% 79.35%
        def helper(sample):
            sample = list(sample)
            out = []
            for i in range(len(sample)):
                if sample[i] == '#' and out:
                    out.pop()
                if sample[i] != '#':
                    out.append(sample[i])
            return out
        return helper(s) == helper(t)
