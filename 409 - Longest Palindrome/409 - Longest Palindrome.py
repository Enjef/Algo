class Solution:
    def longestPalindrome(self, s: str) -> int:  # 92.46% 93.70%
        s_map = {}
        for i in s:
            if i not in s_map:
                s_map[i] = 1
            else:
                s_map[i] += 1
        out = 0
        odd = False
        for key in s_map:
            if s_map[key] % 2 != 0:
                out += s_map[key] - 1
                odd = True
            else:
                out += s_map[key]
        if odd:
            out += 1
        return out

    def longestPalindrome_set(self, s: str) -> int:  # 92.46% 93.70%
        s_set = set()
        for i in s:
            if i not in s_set:
                s_set.add(i)
            else:
                s_set.remove(i)
        return len(s) if not s_set else len(s) - len(s_set) + 1

    def longestPalindrome_study_plan_ds_day_6(
            self,
            s: str) -> int:  # 49.29% 54.72%
        c_dict = {}
        out = 0
        spare_one = False
        for char in s:
            c_dict[char] = c_dict.get(char, 0) + 1
        for item in c_dict:
            if c_dict[item] % 2 == 0:
                out += c_dict[item]
            else:
                out += c_dict[item] - 1
                spare_one = True
        return out + spare_one
