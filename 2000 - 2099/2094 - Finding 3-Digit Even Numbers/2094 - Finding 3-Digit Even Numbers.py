class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:  # 55.08% 13.77%
        def generate(arr, cur):
            if len(cur) == 3:
                if not cur[-1] % 2:
                    out.add(cur[0]*100+cur[1]*10+cur[2])
                return
            for i in range(len(arr)):
                if not cur and not arr[i]:
                    continue
                generate(arr[:i]+arr[i+1:], cur+[arr[i]])
            return

        out = set()
        counter = defaultdict(int)
        for digit in digits:
            if counter[digit] < 3:
                counter[digit] += 1
        digits = []
        for key, val in counter.items():
            digits.extend([key]*val)
        generate(digits, [])
        return sorted(out)

    def findEvenNumbers_best_speed(self, digits: List[int]) -> List[int]:
        result = []
        counts = collections.Counter(digits)
        digits = sorted(counts.keys())
        for digit_1 in digits:
            if digit_1 == 0:
                continue
            for digit_2 in digits:
                if digit_1 == digit_2:
                    if counts[digit_1] < 2:
                        continue
                for digit_3 in digits:
                    if digit_3 % 2 != 0:
                        continue
                    if digit_3 == digit_2:
                        if digit_3 == digit_1:
                            if counts[digit_1] < 3:
                                continue
                        if counts[digit_2] < 2:
                            continue
                    elif digit_3 == digit_1:
                        if counts[digit_1] < 2:
                            continue
                    result.append(int(f'{digit_1}{digit_2}{digit_3}'))
        return result

    def findEvenNumbers_2nd_best_speed(self, digits: List[int]) -> List[int]:
        ans, cnt = [], Counter(digits)
        for i in range(1, 10):
            for j in range(0, 10):
                for k in range(0, 10, 2):
                    if cnt[i] > 0 and cnt[j] > (i == j) and cnt[k] > (k == j) + (k == i):
                        ans.append(i*100 + j*10 + k*1)
        return ans

    def findEvenNumbers_best_memory(self, digits: List[int]) -> List[int]:
        perm = set(permutations(digits, 3))
        s = ''
        l = []
        for i in perm:
            if i[2] % 2 == 0 and i[0] != 0:
                s += str(i[0])+str(i[1])+str(i[2])
                l.append(s)
            s = ''
        return sorted(l)

    def findEvenNumbers_2nd_best_memory(self, digits: List[int]) -> List[int]:
        result, cnt = [], collections.Counter(digits)
        for i in range(1, 10):
            for j in range(10):
                for k in range(0, 10, 2):
                    if cnt[i] > 0 and cnt[j] > (j == i) and cnt[k] > (k == i) + (k == j):
                        result.append(i*100 + j*10 + k)
        return result
