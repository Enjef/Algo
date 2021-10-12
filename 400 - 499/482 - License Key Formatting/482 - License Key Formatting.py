class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
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
