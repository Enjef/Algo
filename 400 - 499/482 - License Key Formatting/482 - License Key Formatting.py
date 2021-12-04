class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:  # 40.50% 97.68%
        s = s.replace('-', '').upper()
        if len(s) < k:
            return s
        size = len(s)
        out = ''
        while size >= k:
            if out:
                out = s[size-k:size] + '-' + out
            else:
                out += s[size-k:size]
            size -= k
        if size:
            out = s[:size] + '-' + out
        return out

    def licenseKeyFormatting_mock(
            self,
            s: str,
            k: int) -> str:  # 47.42% 78.01%
        out = ''
        dash = 0
        for i, char in enumerate(s[::-1]):
            if char == '-':
                continue
            out += char.upper()
            if (len(out) - dash) % k == 0:
                out += '-'
                dash += 1
        if out and out[-1] == '-':
            return out[:-1][::-1]
        return out[::-1]

    def licenseKeyFormatting_mock_v2(
            self,
            s: str,
            k: int) -> str:  # 69.05% 59.50%
        out = ''
        s = s.replace('-', '').upper()
        for index in range(len(s)%k):
            out = out + s[index]
        if not out:
            index = -1
            dash = k
        else:
            index = len(out) - 1
            dash = 0
        for i in range(index+1, len(s)):
            if not dash:
                out = out + '-'
                dash = k
            out = out + s[i]
            dash = dash - 1
        return out
