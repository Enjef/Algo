class Solution:
    def freqAlphabets(self, s: str) -> str:  # 76.24% 84.16%
        first = dict(
            zip([str(x) for x in range(1, 27)],
            'abcdefghijklmnopqrstuvwxyz'))
        n = len(s)
        i = n - 1
        out = []
        while i > -1:
            if s[i] == '#':
                out.append(first[s[i-2:i]])
                i -= 2
            else:
                out.append(first[s[i]])
            i -= 1
        return ''.join(out[::-1])
