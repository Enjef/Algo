alf = {
    'A': 'B',
    'B': 'C',
    'C': 'D',
    'D': 'E',
    'E': 'F',
    'F': 'G',
    'G': 'H',
    'H': 'I',
    'I': 'J',
    'J': 'K',
    'K': 'L',
    'L': 'M',
    'M': 'N',
    'N': 'O',
    'O': 'P',
    'P': 'Q',
    'Q': 'R',
    'R': 'S',
    'S': 'T',
    'T': 'U',
    'U': 'V',
    'V': 'W',
    'W': 'X',
    'X': 'Y',
    'Y': 'Z',
    'Z': 'A'
}


class Solution:

    # time limit exceeded
    def convertToTitle_1(self, columnNumber: int) -> str:
        out = 'A'
        for _ in range(columnNumber - 1):
            out = out[:-1] + alf[out[-1]]
            if out[-1] != 'A':
                continue
            else:
                if len(out) > 1:
                    for i in range(len(out) - 2, -1, -1):
                        out = out[:i] + alf[out[i]] + out[i+1:]
                        if out[i] != 'A':
                            break
                        if out[i] == 'A':
                            continue
                    if out[0] == 'A':
                        out = 'A' + out
                else:
                    out = 'A' + out
        return out

    def convertToTitle(self, columnNumber: int) -> str:
        char_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if columnNumber == 1:
            return 'A'
        temp = columnNumber
        out = ''
        while temp:
            temp -= 1
            out += char_str[temp % 26]
            temp //= 26
        return out[::-1]


x = Solution()
print('final', x.convertToTitle(701))
