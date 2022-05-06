class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:  # 80.88% 71.18%
        out = []
        out.append(s[:spaces[0]])
        for i in range(len(spaces)-1):
            out.append(s[spaces[i]:spaces[i+1]])
        out.append(s[spaces[-1]:])
        return ' '.join(out)

    def addSpaces_v2(self, s: str, spaces: List[int]) -> str:  # 54.41 % 7.94%
        out = []
        spaces = set(spaces)
        for i, char in enumerate(s):
            if i in spaces:
                out.append(' ')
            out.append(char)
        return ''.join(out)

    def addSpaces_best_speed(self, s: str, spaces: List[int]) -> str:
        l = []
        i = 0
        for x in spaces:
            z = s[i:x]
            l.append(z)
            i = x
        z = s[i:]
        l.append(z)
        return ' '.join(l)

    def addSpaces_best_memory(self, s: str, spaces: List[int]) -> str:
        ans = []
        i = len(s) - 1
        while i >= 0:
            ans.append(s[i])
            if spaces and i == spaces[-1]:
                ans.append(' ')
                spaces.pop()
            i -= 1
        return ''.join(ans[:: -1])
