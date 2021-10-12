class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:  # 29.09% 19.20%
        def helper(sample):
            count = 0
            sample = list(sample[::-1])
            out = []
            for i in range(len(sample)):
                if sample[i] == '#':
                    count += 1
                elif sample[i] != '#' and count:
                    count -= 1
                else:
                    out += sample[i]
            return out
        return helper(s) == helper(t)

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

    def backspaceCompare_best_speed(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        s_pound = 0
        t_pound = 0
        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == "#":
                    s_pound += 1
                    i -= 1
                elif s_pound > 0:
                    s_pound -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if t[j] == "#":
                    t_pound += 1
                    j -= 1
                elif t_pound > 0:
                    t_pound -= 1
                    j -= 1
                else:
                    break
            if (i >= 0) != (j >= 0):
                return False
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            i -= 1
            j -= 1
        return True

    def backspaceCompare_best_memory(self, s: str, t: str) -> bool:
        stackS = []
        for i in range(len(s)):
            if s[i] == '#':
                if stackS:
                    stackS.pop()
            else:
                stackS.append(s[i])
        stackT = []
        for i in range(len(t)):
            if t[i] == '#':
                if stackT:
                    stackT.pop()
            else:
                stackT.append(t[i])
        return stackS == stackT
