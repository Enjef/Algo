class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)
        potions.sort()
        out = [0]*n
        for i, spell in enumerate(spells):
            cur_idx = bisect_left(potions, success/spell, 0, len(potions)-1)
            cur = potions[cur_idx]
            if cur*spell >= success:
                out[i] = m - cur_idx
        return out

    def successfulPairs_v2(self, spells: List[int], potions: List[int], success: int) -> List[int]:  # 28.57% 57.14% (57.14% 57.14%)
        return (potions.sort(),
        [len(potions)-bisect_left(potions, success/spell, 0, len(potions)-1) if (potions[bisect_left(potions, success/spell, 0, len(potions)-1)])*spell >= success else 0 for spell in spells])[1]

    def successfulPairs_lee215(self, spells, potions, success):
        potions.sort()
        return [len(potions) - bisect_left(potions, (success + a - 1) // a) for a in spells]
