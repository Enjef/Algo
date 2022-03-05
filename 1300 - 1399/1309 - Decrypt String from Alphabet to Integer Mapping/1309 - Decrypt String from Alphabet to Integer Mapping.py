from string import ascii_lowercase


class Solution:
    def freqAlphabets(self, s: str) -> str:  # 65.24%  94.04 %
        c_map = 'abcdefghijklmnopqrstuvwxyz'
        out = ''
        i = len(s)-1
        while i > -1:
            if s[i] == '#':
                out = c_map[int(s[i-2:i])-1] + out
                i -= 2
            else:
                out = c_map[int(s[i])-1] + out
            i -= 1
        return out

    def freqAlphabets_best_old(self, s: str) -> str:
        d = {}
        for i, c in enumerate(ascii_lowercase, 1):
            d[i] = c
        s_out = ''
        pointer = len(s)-1
        while pointer >= 0:
            if s[pointer] == '#':
                s_out += d[int(s[pointer-2:pointer])]
                pointer -= 3
            else:
                s_out += d[int(s[pointer])]
                pointer -= 1
        return s_out[::-1]

    def freqAlphabets_best_speed(self, s: str) -> str:
        ans = ''
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                ans += chr(int(s[i:i + 2]) + ord('a') - 1)
                i += 3
            else:
                ans += chr(int(s[i]) + ord('a') - 1)
                i += 1
        return ans
