class Solution:
    # 55.56% 33.11% (9.93% 33.11%)
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)

    # 83.70% 33.11% (89.57% 33.11%)
    def arrayStringsAreEqual_v2(self, word1: List[str], word2: List[str]) -> bool:
        def chars(word):
            for el in word:
                for char in el:
                    yield char

        first = chars(word1)
        second = chars(word2)
        while True:
            a = b = None
            try:
                a = next(first)
            except:
                pass
            try:
                b = next(second)
                if a != b:
                    return False
            except:
                break
        return a == b


class Solution_best_speed:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a = ''.join(word1)
        b = ''.join(word2)
        if a == b:
            return True
        else:
            return False
