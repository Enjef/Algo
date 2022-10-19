class Solution:
    # 68.30% 70.61% (64.45% 99.46%)
    def largestPalindromic(self, num: str) -> str:
        count = Counter(str(num))
        mid_max = ''
        pairs = []
        for key, val in count.items():
            if val == 1:
                mid_max = max(mid_max, key)
            else:
                pairs.append(key)
        pairs.sort()
        for i in range(len(pairs)-1, -1, -1):
            if count[pairs[i]] % 2:
                mid_max = max(mid_max, pairs[i])
                break
        res = ''.join([x*(count[x]//2) for x in pairs])
        res = res[::-1] + mid_max + res
        res = res.strip('0')
        return res if res else '0'


class Solution_best_speed:
    def largestPalindromic(self, num: str) -> str:
        c = Counter(num)
        res = ''.join(c[i]//2*i for i in '9876543210').lstrip('0')
        m = max(c[i] % 2*i for i in c)
        return res+m+res[::-1] or '0'


class Solution_best_memory:
    def largestPalindromic(self, num: str) -> str:
        counts = [0] * 10
        for char in num:
            idx = ord(char) - ord('0')
            counts[idx] += 1
        left_components = [str(idx) * (counts[idx] // 2) for idx in reversed(range(10))]
        middle = ''
        for idx in reversed(range(10)):
            if counts[idx] % 2 != 0:
                middle = str(idx)
                break
        left = ''.join(left_components)
        right = ''.join(reversed(left_components))
        return ''.join([left, middle, right]).strip('0') or '0'
