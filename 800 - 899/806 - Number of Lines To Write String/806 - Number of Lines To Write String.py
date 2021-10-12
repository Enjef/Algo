class Solution:
    def numberOfLines(
            self,
            widths: List[int],
            s: str) -> List[int]: # 69.39% 21.57%
        alph = {
            key: value for key, value in
            zip('abcdefghijklmnopqrstuvwxyz', widths)
        }
        line = 1
        cur = 0
        for char in s:
            if cur + alph[char] > 100:
                line += 1
                cur = alph[char]
            else:
                cur += alph[char]
        return [line, cur]

    def numberOfLines_best(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        lastwidth = 0
        for i in s:
            width = widths[string.ascii_lowercase.index(i)]
            if lastwidth + width > 100:
                lines += 1
                lastwidth = width
            else:
                lastwidth += width
        return lines, lastwidth

    def numberOfLines_bst_memory(self, widths: List[int], s: str) -> List[int]:
        cnt = 1
        cur = 0
        for c in s:
            w = widths[ord(c)-ord('a')]
            cur += w
            if cur > 100:
                cnt += 1
                cur = w
        return [cnt, cur]
