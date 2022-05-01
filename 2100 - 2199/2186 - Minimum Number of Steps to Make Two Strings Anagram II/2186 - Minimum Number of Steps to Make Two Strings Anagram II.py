class Solution:
    def minSteps(self, s: str, t: str) -> int:  # 12.14% 99.44%
        count_s = defaultdict(int)
        count_t = defaultdict(int)
        for char in s:
            count_s[char] += 1
        for char in t:
            count_t[char] += 1
        result = 0
        for char in set(count_s.keys()) | set(count_t.keys()):
            if char not in count_s:
                result += count_t[char]
            elif char not in count_t:
                result += count_s[char]
            else:
                result += abs(count_s[char]-count_t[char])
        return result

    def minSteps_v2(self, s: str, t: str) -> int:  # 43.27% 88.22%
        counter = defaultdict(int)
        for char in s:
            counter[char] += 1
        for char in t:
            counter[char] -= 1
        return sum([abs(x) for x in counter.values()])

    def minSteps_best_speed(self, s: str, t: str) -> int:
        return sum(abs(s.count(c) - t.count(c)) for c in string.ascii_lowercase)

    def minSteps_2nd_best_speed(self, s: str, t: str) -> int:
        n = len(s) + len(t)
        for i in set(s):
            n -= min(s.count(i), t.count(i)) * 2
        return n

    def minSteps_4th(self, s: str, t: str) -> int:
        cc = 0
        for c in 'abcdefghijklmnopqrstuvwxyz':
            cc += abs(s.count(c) - t.count(c))
        return cc

    def minSteps_best_memory(self, s: str, t: str) -> int:
        d, n = [0]*26, ord('a')
        for c in s:
            d[ord(c)-n] += 1
        for c in t:
            d[ord(c)-n] -= 1
        return sum([abs(x) for x in d])
