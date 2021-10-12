map_b = {
    '000': '00',
    '010': '10',
    '100': '10',
    '110': '01',
    '001': '10',
    '011': '01',
    '101': '01',
    '111': '11',
}


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        out = ''
        ext = '0'
        if len(a) > len(b):
            a, b = b, a
        for i in range(1, len(a)+1):
            char = map_b[a[-i]+b[-i]+ext]
            out = char[0] + out
            ext = char[1]
        if len(out) < len(b):
            if not ext:
                return b[:-len(a)-1] + out
            for i in range(len(b)-len(a)-1, -1, -1):
                char = map_b['0'+b[i]+ext]
                out = char[0] + out
                ext = char[1]
        if ext == '0':
            return out
        return ext + out

    def addBinary_best(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2)).replace("0b", "")
