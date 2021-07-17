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
            print(i, c)
            cur_end = max(cur_end, end[c])
            if cur_end == i:
                ans.append(cur_end - cur_start + 1)
                cur_start = i + 1
                cur_end = i + 1
        return ans
