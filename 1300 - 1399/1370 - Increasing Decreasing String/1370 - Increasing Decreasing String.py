class Solution:
    def sortString(self, s: str) -> str:  # 27.91% 11.22%
        out = ''
        s_set = list(set(s))
        s_set = sorted(s_set) + sorted(s_set, reverse=True)
        s = list(s)
        while s:
            for char in s_set:
                if char not in s:
                    continue
                s.remove(char)
                out += char
                if not s:
                    break
        return out

    def sortString_hash(self, s: str) -> str:  # 85.97% 41.23%
        out = ''
        x_map = {}
        for i in s:
            if i not in x_map:
                x_map[i] = 0
            x_map[i] += 1
        step = 1
        count = sum(x_map.values())
        while count:
            for char in sorted(x_map)[::step]:
                if x_map[char]:
                    x_map[char] -= 1
                    out += char
                    count -= 1
            step = -step
        return out
