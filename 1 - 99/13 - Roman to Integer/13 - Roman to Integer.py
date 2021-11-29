symb_dist = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


class Solution:
    def romanToInt(self, s: str) -> int:  # 98.31% 
        out = 0
        temp = symb_dist[s[0]]
        prev = s[0]
        for char in s[1:]:
            if char == prev:
                temp += symb_dist[char]
                continue
            if symb_dist[char] > symb_dist[prev]:
                out += symb_dist[char] - temp
                temp = 0
                prev = char
                continue
            prev = char
            out += temp
            temp = symb_dist[char]
        out += temp
        return out

class Solution_mock:
    def romanToInt(self, s: str) -> int:  # 71.39% 28.64%
        roman = {           
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        cur_char = s[0]
        cur = roman[cur_char]
        total = 0
        for char in s[1:]:
            if roman[char] > roman[cur_char]:
                total -= cur
                cur_char = char
                cur = roman[cur_char]
            elif roman[char] < roman[cur_char]:
                total += cur
                cur = roman[char]
                cur_char = char
            else:
                cur += roman[char]
                cur_char = char
        total += cur
        return total

class Solution_best_speed:
    def romanToInt(self, s: str) -> int:
        # O(n), use a stack to keep track of preceeding values
        # IX -> 9 Increasing mag so subtract
        # XI -> 11 Decreasing mag so add
        values = {
            "M": 1000, 
            "D": 500, 
            "C": 100, 
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }
        total_sum = 0 # 1994
        prev = math.inf # 1
        # "MCMXCIV"
        for char in s:
            curr = values[char] # 5
            if curr > prev: # False
                total_sum -= (2 * prev) # 20
                total_sum += curr # 100
            else:
                total_sum += curr
            prev = curr 
        return total_sum

class Solution_3d_best_speed:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        n = len(s)
        result = roman_map[s[n-1]]
        for i in range(n-1):
            if roman_map[s[n-i-1]] <= roman_map[s[n-i-2]]:
                result = result + roman_map[s[n-i-2]]
            else:
                result = result - roman_map[s[n-i-2]]
        return result

I, V, X, L, C, D, M = "IVXLCDM"
VALUES = {I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000}

class Solution_best_memory:
    def romanToInt(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return VALUES[s]
        # if s[:2] in (I+V, I+X, X+L, X+C, C+D, C+M):
        if s[:2] in 'IV IX XL XC CD CM':
            return VALUES[s[1]] - VALUES[s[0]] + self.romanToInt(s[2:])
        return VALUES[s[0]] + self.romanToInt(s[1:])

class Solution_2nd_best_memory:
    def romanToInt(self, s: str) -> int:
        m = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50
             ,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
        left = 0
        sum = 0
        while left < len(s):
            if left + 2 <= len(s) and s[left:left+2] in m:
                sum += m[s[left:left+2]]
                left += 2
            else:
                sum += m[s[left:left+1]]
                left += 1
        return sum
