class Solution:
    # 84.32% 9.57% (22.91% 9.57%)
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift = [ord(s[i])-97 for i in range(n)]
        events = []
        for start, end, direction in shifts:
            events.extend(
                [(start, 1), (end+1, -1)] if direction else
                [(start, -1), (end+1, 1)]
            )
        events.sort()
        d = defaultdict(int)
        for event, direction in events:
            if event > n-1:
                break
            d[event] += direction
        cur = 0
        for i in range(n):
            if i in d:
                cur += d[i]
            shift[i] += cur
        return ''.join(chr((shift[i] % 26)+ord('a')) for i in range(len(s)))


class Solution_best_speed:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        sz = [0] * (len(s) + 1)
        for start, end, dir in shifts:
            if dir == 1:
                sz[start] += 1
                sz[end + 1] -= 1
            else:
                sz[start] -= 1
                sz[end + 1] += 1
        return ''.join(chr(((ord(c) - 97) + shift) % 26 + 97) for c, shift in zip(s, accumulate(sz)))

    def shiftingLetters_2nd(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * len(s)
        for start, end, direction in shifts:
            prefix[start] += 1 if direction else -1
            if end + 1 < len(s):
                prefix[end + 1] -= 1 if direction else -1
        cur_sum = 0
        prefix_sum = []
        for p in prefix:
            cur_sum += p
            prefix_sum.append(cur_sum % 26)

        def addAlpha(a, n):
            o = ord(a) + n
            if o > ord('z'):
                o -= 26
            return chr(o)

        return ''.join([addAlpha(a, prefix_sum[i]) for i, a in enumerate(s)])


class Solution_best_memory:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        for term in shifts:
            if term[-1] == 0:
                term[-1] = -1
        shifts.sort(reverse=True)
        stack, cur = [], 0
        res = []
        for i in range(n):
            while shifts and i >= shifts[-1][0]:
                cur += shifts[-1][-1]
                temp = shifts.pop()[1:]
                bisect.insort(stack, [-temp[0], temp[1]])
            while stack and stack[-1][0] > -i:
                cur -= stack[-1][-1]
                stack.pop()
            res.append(cur)

        def foo(lt, y):
            x = ord(lt)
            temp = (x-97 + y) % 26
            return chr(temp+97)

        return ''.join([foo(lt, y) for (lt, y) in zip(s, res)])

    def shiftingLetters_2nd(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shifts.sort(reverse=True)
        delta = 0
        forwards = []
        backwards = []
        transformed_s = [ord(c) for c in s]
        for i in range(n):
            while shifts and shifts[-1][0] == i:
                start, end, direction = shifts[-1]
                if direction == 1:
                    heappush(forwards, end)
                    delta += 1
                else:
                    heappush(backwards, end)
                    delta -= 1
                shifts.pop()
            transformed_s[i] = ((transformed_s[i] - 97 + delta) % 26) + 97
            while forwards and forwards[0] == i:
                heappop(forwards)
                delta -= 1
            while backwards and backwards[0] == i:
                heappop(backwards)
                delta += 1
        return ''.join([chr(num) for num in transformed_s])

    def shiftingLetters_3d(self, s: str, shifts: List[List[int]]) -> str:
        shifts.sort(reverse=True)
        hp = []
        ans = ''
        cnt = 0
        for i, c in enumerate(s):
            while shifts and shifts[-1][0] == i:
                a, b, m = shifts.pop()
                m = 1 if m else -1
                cnt += m
                heappush(hp, (b+1, m))
            while hp and hp[0][0] == i:
                cnt -= heappop(hp)[1]
            ans += chr((ord(c) - ord('a') + cnt) % 26 + ord('a'))
        return ans

    def shiftingLetters_6th(self, s: str, shifts: List[List[int]]) -> str:
        cum_shifts = [0 for _ in range(len(s)+1)]
        for st, end, d in shifts:
            if d == 0:
                cum_shifts[st] -= 1
                cum_shifts[end+1] += 1
            else:
                cum_shifts[st] += 1
                cum_shifts[end+1] -= 1
        cum_sum = 0
        for i in range(len(s)):
            cum_sum += cum_shifts[i]
            new_code = (((ord(s[i]) + cum_sum) - 97) % 26) + 97
            s = s[:i] + chr(new_code) + s[i+1:]
        return s
