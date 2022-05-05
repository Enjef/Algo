class Solution:
    def digitSum(self, s: str, k: int) -> str:  # 9.97% 66.16%
        while len(s) > k:
            new = []
            for i in range(0, len(s), k):
                new.append(sum(map(int, s[i:i+k])))
            s = ''.join(map(str, new))
        return ''.join(map(str, s))

    def digitSum_best_speed(self, s: str, k: int) -> str:
        def rp(s: str):
            res = 0
            for i in s:
                res += int(i)
            return str(res)

        while len(s) > k:
            temp = ''
            for i in range(0, len(s), k):
                if i + k in range(len(s)):
                    ans = rp(s[i:i+k])
                else:
                    ans = rp(s[i:])
                temp += ans
            s = temp
        return s

    def digitSum_2nd_best_speed(self, s: str, k: int) -> str:
        while len(s) > k:
            t = ''
            for i in range(0, len(s), k):
                tt = 0
                for n in s[i:i+k]:
                    tt += int(n)
                t += str(tt)
            s = t
        return s

    def digitSum_best_memory(self, s: str, k: int) -> str:
        while len(s) > k:
            set_3 = [s[i:i+k] for i in range(0, len(s), k)]
            s = ''
            for e in set_3:
                s += str(sum([int(n) for n in e]))
        return s
