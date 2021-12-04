class Solution:
    def partitionLabels(self, s: str) -> List[int]:  # 99.37% 56.71%
        coords = {}
        for i in range(len(s)):
            if s[i] in coords:
                coords[s[i]][1] = i
            else:
                coords[s[i]] = [i, i]
        parts = sorted(coords.values())
        out = [parts[0][1]-parts[0][0]+1]
        cur = parts[0][1]
        for i in range(1, len(parts)):
            if parts[i][1] < cur:
                continue
            elif parts[i][0] < cur:
                out[-1] += parts[i][1] - cur
                cur = parts[i][1]
            else:
                out.append(parts[i][1] - cur)
                cur = parts[i][1]
        return out
