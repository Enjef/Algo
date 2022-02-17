class Solution:
    def checkString(self, s: str) -> bool: # 29.79% 99.70%
        a = False
        b = False
        for i, char in enumerate(s):
            if char == 'a':
                a = i
            else:
                b = i
            if a and b and a > b:
                return False
        return a is False or b is False or a < b

    def checkString_best_speed(self, s: str) -> bool:
        a_arr = []
        b_arr = []
        for index, letter in enumerate(s): 
            if letter == 'a': 
                a_arr.append(index)
        for index, letter in enumerate(s): 
            if letter == 'b': 
                b_arr.append(index)
        if len(a_arr) == 0 or len(b_arr) == 0:
            return True
        max_a = max(a_arr)
        min_b = min(b_arr)
        if min_b < max_a: 
            return False
        else: 
            return True

    def checkString_2nd_best_speed(self, s: str) -> bool:
        seen = set()
        for c in s:
            if c == 'a' and 'b' in seen:
                return False
            if c not in seen: 
                seen.add(c)
        return True

    def checkString_best_memory(self, s):
        if len(set(s)) == 1:
            return True
        ss = s.split('ab')
        return (len(ss) == 2) and ('b' not in ss[0]) and ('a' not in ss[1])

    def checkString_2nd_best_memory(self, s: str) -> bool:
        return True if str.join("", sorted(s)) == s else False
