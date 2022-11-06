class Solution:
    # 73.38% 98.81%
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            target = min(s)
            splits = [i for i, char in enumerate(s) if char == target]
            return min(s[idx:]+s[:idx] for idx in splits)
        return ''.join(sorted(s))


class Solution_best_speed(object):
    def orderlyQueue(self, S, K):
        n = len(S)
        if K == 0:
            return S
        if K == 1:
            smallest = S
            for i in range(1, n):
                new_str = S[: K - 1] + S[K:] + S[K - 1]
                if new_str < smallest:
                    smallest = new_str
                S = new_str
            return smallest
        if K >= 2:
            return ''.join(sorted(S))


class Solution_best_memory:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        else:
            return ''.join(sorted(s))
