class Solution:
    def minSteps(self, s: str, t: str) -> int:  # 46.89% 79.54%
        res = dict(zip(set(s+t), [0]*len(set(s+t))))
        for char in s:
            res[char] = res.get(char, 0) + 1
        for char in t:
            res[char] = res.get(char, 0) - 1
        out = sum([abs(x) for x in res.values()])
        return out // 2

    def minSteps_best_speed(self, s: str, t: str) -> int:
        dict_s = {}
        dict_t = {}
        all_letters = 'abcdefghijklmnopqrstuvwxyz'
        comp = 0
        for letter in all_letters:
            dict_s[letter] = s.count(letter)
            dict_t[letter] = t.count(letter)
            comp += abs(dict_s[letter]-dict_t[letter])
        return int(comp/2)

    def minSteps_2nd_best_speed(self, s: str, t: str) -> int:
        count = 0
        for i in set(s):
            count_s = s.count(i)
            count_t = t.count(i)
            if count_s > count_t:
                count += (count_s - count_t)
        return count

    def minSteps_best_memory(self, s: str, t: str) -> int:
        for ch in s:
            t = t.replace(ch, '', 1)
        return len(t)

    def minSteps_2nd_best_memory(self, s: str, t: str) -> int:
        count = [0]*26
        for c in s:
            count[ord(c)-ord('a')] += 1
        ans = 0
        for c in t:
            idx = ord(c)-ord('a')
            if count[idx] > 0:
                count[idx] -= 1
            else:
                ans += 1
        return ans
