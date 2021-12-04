class Solution:
    def partitionLabels(self, s: str):  # 5.10% 55.73%
        x_map = [[s[0]]]
        for i in range(1, len(s)):
            first = -1
            for j in range(len(x_map)):
                if s[i] in x_map[j]:
                    first = j
                    break
            if first > -1:
                temp = []
                for k in range(first, len(x_map)):
                    temp += x_map[k]
                temp.append(s[i])
                x_map = x_map[:first] + [temp]
            else:
                x_map.append([s[i]])
        return [len(i) for i in x_map]

    def partitionLabels_two(self, s: str):  # 72.76% 55.57%
        end = {}
        for i, c in enumerate(s):
            end[c] = i
        ans = []
        cur_start = 0
        cur_end = 0
        print(end)
        for i, c in enumerate(s):
            cur_end = max(cur_end, end[c])
            if cur_end == i:
                ans.append(cur_end - cur_start + 1)
                cur_start = i + 1
                cur_end = i + 1
        return ans

    def partitionLabels_ds_day_7(self, s: str) -> List[int]:  # 99.37% 56.71%
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

    def partitionLabels_best_memory(self, s: str) -> List[int]:
        ret = []
        d = {}
        for i in range(len(s)):
            d[s[i]] = i
        end = 0
        count = 0
        for i in range(len(s)):
            end = max(end, d[s[i]])
            count += 1 
            if i == end:
                ret.append(count)
                count = 0
        return ret
