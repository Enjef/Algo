class Solution:
    def numOfStrings(self, patterns, word: str) -> int: # 41.46% 94.82%
        out = 0
        for patterns in patterns:
            if patterns in word:
                out += 1
        return out

    def numOfStrings_best_speed(self, patterns: List[str], word: str) -> int:
        return len([i for i in patterns if i in word])

    def numOfStrings_best_memory(self, patterns: List[str], word: str) -> int:
        def isValid(string1, string2):
            l1 = len(string1)
            l2 = len(string2)
            if l1 > l2:
                return False
            if string1 in string2:
                return True
            return False
        res = 0
        for pattern in patterns:
            if isValid(pattern, word):
                res += 1
        return res
