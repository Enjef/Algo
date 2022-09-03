class Solution:
    # 37.07% 41.16%
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        cur = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        while cur:
            new = set()
            for el in cur:
                if el % 10+k < 10:
                    new.add(el*10+el % 10+k)
                if el % 10-k > -1:
                    new.add(el*10+el % 10-k)
            if new:
                check = new.pop()
                new.add(check)
                if len(str(check)) == n:
                    return new
            cur = new
        return cur

    # 56.46% 41.16%
    def numsSameConsecDiff_v2(self, n: int, k: int) -> List[int]:
        cur = {str(x) for x in range(1, 10)}
        while cur:
            new = set()
            for el in cur:
                if int(el[-1])+k < 10:
                    new.add(el + str(int(el[-1])+k))
                if int(el[-1])-k > -1:
                    new.add(el + str(int(el[-1])-k))
            if new:
                check = new.pop()
                new.add(check)
                if len(check) == n:
                    return new
            cur = new
        return cur

    # 96.60% 41.16%
    def numsSameConsecDiff_v3(self, n: int, k: int) -> List[int]:
        cur = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        while cur:
            new = set()
            for el in cur:
                temp = el % 10
                if temp+k < 10:
                    new.add(el*10+temp+k)
                if temp-k > -1:
                    new.add(el*10+temp-k)
            if new:
                check = new.pop()
                new.add(check)
                if len(str(check)) == n:
                    return new
            cur = new
        return cur

    def numsSameConsecDiff_best_speed(self, n: int, k: int) -> List[int]:
        numset = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for i in range(n - 1):
            res = []
            for num in numset:
                cur = num % 10
                if cur + k <= 9:
                    res.append(num * 10 + cur + k)
                if k != 0 and cur - k >= 0:
                    res.append(num * 10 + cur - k)
            numset = res
        return res

    def numsSameConsecDiff_2nd_best_speed(self, n: int, k: int) -> List[int]:
        graph = defaultdict(list)
        for i in range(0, 10):
            if i-k >= 0:
                graph[i].append(i-k)
            if i +k < 10:
                graph[i].append(i+k)
        start = [i for i in graph if i!= 0]
        for j in range(n-1):
            new = set()
            for i in start:
                last = i%10
                for k in graph[last]:
                    new.add(i*10 + k)
            start = new
        return list(start)

    def numsSameConsecDiff_best_memory(self, n: int, k: int) -> List[int]:
        res = []
        stack = deque((1, num) for num in range(1, 10))
        while stack:
            curr_pos, curr_num = stack.pop()
            if curr_pos == n:
                res.append(curr_num)
            else:
                last_digit = curr_num % 10
                next_pos = curr_pos + 1
                candidates = (last_digit + k, last_digit - k) if k\
                              else (last_digit,)
                for digit in candidates:
                    if digit in range(10):
                        stack.append((next_pos, curr_num * 10 + digit))
        return res
