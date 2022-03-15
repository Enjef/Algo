class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:  # 18.38% 32.58%
        return sum([word.startswith(pref) for word in words])

    def prefixCount_v2(self, words, pref): # 5.22% 97.30%
        count = 0
        for word in words:
            count += word.startswith(pref)
        return count

    def prefixCount_best_speed(self, words: List[str], pref: str) -> int:
        return sum(
            [1 for word in words if
                (len(word) >= len(pref) and word[: len(pref)] == pref)])

    def prefixCount_second_best_speed(self, words, pref):
        cont = 0
        for word in words:
            if word.find(pref, 0) == 0:
                cont += 1
        return cont
