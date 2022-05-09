class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:  # 67.17% 77.31%
        start = dict()
        result = float('inf')
        for i, card in enumerate(cards):
            if card in start:
                result = min(result, i-start[card]+1)
            start[card] = i
        return result if result != float('inf') else -1

    def minimumCardPickup_best_speed(self, cards: List[int]) -> int:
        ans = inf
        seen = {}
        for i, x in enumerate(cards):
            if x in seen:
                ans = min(ans, i - seen[x] + 1)
            seen[x] = i
        return ans if ans < inf else -1

    def minimumCardPickup_memory_best(self, cards: List[int]) -> int:
        hashset = set()
        left = 0
        n = len(cards)
        res = float('inf')
        for i in range(n):
            while cards[i] in hashset:
                res = min(res, i - left + 1)
                hashset.remove(cards[left])
                left += 1
            hashset.add(cards[i])
        return res if res != float('inf') else -1
