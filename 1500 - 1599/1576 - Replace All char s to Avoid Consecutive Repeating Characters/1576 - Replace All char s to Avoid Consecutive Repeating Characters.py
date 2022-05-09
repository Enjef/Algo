class Solution:
    def modifyString(self, s: str) -> str:  # 16.67% 22.40%
        alp = set('abcdefghijklmnopqrstuvwxyz')
        out = []
        for i, char in enumerate(s):
            neighbours = set()
            if char == '?':
                if i > 0:
                    neighbours.add(out[i-1])
                if i < len(s) - 1:
                    neighbours.add(s[i+1])
                out.append((alp-neighbours).pop())
            else:
                out.append(char)
        return ''.join(out)

    def modifyString_best_speed(self, s: str) -> str:
        def rec(s, r):
            if not s:
                self.res = r
                return True
            if s[0] == '?':
                for i in range(26):
                    if not r or r[-1] != chr(ord('a')+i):
                        if rec(s[1:], r+chr(ord('a')+i)):
                            return True
                return False
            if r and r[-1] == s[0]:
                return False
            r += s[0]
            return rec(s[1:], r)

        rec(s, '')
        return self.res

    def modifyString_2nd_best_speed(self, s: str) -> str:
        s_len = len(s)
        for i in range(s.count('?')):
            index = s.find('?')
            for char in 'abc':
                if (index == 0 or s[index - 1] != char) and (index + 1 == s_len or s[index + 1] != char):
                    s = s.replace('?', char, 1)
                    break
        return s

    def modifyString_3d_best_speed(self, s: str) -> str:
        res = ''
        left = right = 0
        
        def nextChar(a: str) -> str:
            return chr(ord('a') + (ord(a) - ord('a') + 1) % 26)

        while left < len(s):
            while right < len(s) and s[right] == '?':
                right += 1
            if left < right:
                for i in range(left, right):
                    c = 'a' if i == 0 else nextChar(res[i-1])
                    if i < len(s) - 1 and c == s[i+1]:
                        c = nextChar(c)
                    res += c
                left = right
            else:
                if left < len(s):
                    res += s[left]
                left += 1
                right = left
        return res

    def modifyString_best_memory(self, s: str) -> str:
        N = len(s)
        resp = list(s)
        for i in range(len(resp)):
            if resp[i] == '?':
                for c in 'xyz':
                    if(i == 0 or resp[i-1] != c) and (i == N-1 or resp[i+1] != c):
                        resp[i] = c
                        break   
        return ''.join(resp)
