class Solution:
    def customSortString(self, order: str, s: str) -> str:  # 66.98% 00:00%
        weight = {char: i for i, char in enumerate(order)}
        sor = []
        other = []
        for char in s:
            if char in weight:
                sor.append((char, weight[char]))
            else:
                other.append(char)
        sor.sort(key=lambda x: x[1])
        return ''.join([x[0] for x in sor] + other)

    def customSortString_v2(self, order: str, s: str) -> str:  # 66.98% 54.31%
        counter = {}
        out = ''
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        for char in order:
            out += char * counter.get(char, 0)
            if char in counter:
                counter.pop(char)
        for char, count in counter.items():
            out += char * count
        return out

    def customSortString_best_speed(self, order: str, s: str) -> str:
        orderCount = {}
        residue = ""
        res = ""
        for char in order:
            orderCount[char] = 0
        for char in s:
            if char in order:
                orderCount[char] += 1
            else:
                residue += char
        for char in order:
            res += char * orderCount[char]
        return res + residue

    def customSortString_best_memory(self, order: str, s: str) -> str:
        count = collections.Counter(s)
        ans = []
        for l in order:
            ans.append(l*count[l])
            count[l] = 0
        for l in count:
            ans.append(l*count[l])
        return "".join(ans)
