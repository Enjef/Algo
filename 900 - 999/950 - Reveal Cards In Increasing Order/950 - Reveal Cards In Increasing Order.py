class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        if len(deck) == 1:  # 34.55% 94.91%
            return deck
        deck.sort(reverse=True)
        out = []
        for i in range(len(deck)):
            if len(out) > 1:
                last = out.pop()
                out.insert(0, last)
            out.insert(0, deck[i])
        return out

    def deckRevealedIncreasing_best_speed(self, deck: List[int]) -> List[int]:
        N = len(deck)
        ans = [None for _ in range(N)]
        index = deque(range(N))
        for card in sorted(deck):
            ans[index.popleft()] = card
            if index:
                index.append(index.popleft())
        return ans
