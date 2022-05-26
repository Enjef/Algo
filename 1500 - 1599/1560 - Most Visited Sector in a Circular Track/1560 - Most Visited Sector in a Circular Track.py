class Solution:
    def mostVisited(
            self, n: int, rounds: List[int]) -> List[int]:  # 22.69% 25.00%
        counter = {key: 0 for key in range(1, n+1)}
        counter[rounds[0]] += 1
        for i in range(1, len(rounds)):
            if rounds[i-1] < rounds[i]:
                for j in range(rounds[i-1]+1, rounds[i]+1):
                    counter[j] += 1
            else:
                for j in range(1, rounds[i]+1):
                    counter[j] += 1
                for j in range(rounds[i-1]+1, n+1):
                    counter[j] += 1
        return sorted(
            [key for key in counter if counter[key] == max(counter.values())])

    def mostVisited_best_speed(self, n: int, rounds: List[int]) -> List[int]:
        if rounds[-1] >= rounds[0]:
            return list(range(rounds[0], rounds[-1] + 1))
        else:
            return list(range(1, rounds[-1]+1)) + list(range(rounds[0], n+1))

    def mostVisited_best_mmeory(self, n: int, rounds: List[int]) -> List[int]:
        s, e = rounds[0], rounds[-1]
        res = []
        while e != s:
            res.append(e)
            e -= 1
            if e == 0:
                e = n
        res.append(s)
        return sorted(res)

    def mostVisited_lee215(self, n, A):
        return range(A[0], A[-1] + 1) or range(1, A[-1] + 1) + range(A[0], n + 1)
