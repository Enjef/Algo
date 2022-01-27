class Solution:
    def isAlienSorted(
            self, words: List[str], order: str) -> bool:  # 16.09% 98.25%
        def custom_weight(arr):
            res = []
            for char in arr:
                res.append(weight[char])
            return res
        weight = dict((val, i) for i, val in enumerate(order))
        return words == sorted(words, key=custom_weight)

    def isAlienSorted_best_speed(self, words: List[str], order: str) -> bool:
        word_map = {}
        for i, c in enumerate(order):
            word_map[c] = i
        for x in range(len(words) - 1):
            for y in range(len(words[x])):
                if y >= len(words[x+1]):
                    return False
                if words[x][y] != words[x+1][y]:
                    if word_map[words[x][y]] > word_map[words[x+1][y]]:
                        return False
                    break
        return True

    def isAlienSorted_best_memory(self, words: List[str], order: str) -> bool:
        def compare(str1: str, str2: str) -> bool:
            i = 0
            while (
                i < min(len(str1), len(str2)) and
                order.find(str1[i]) == order.find(str2[i])):
                    i += 1
            if i == len(str1):
                return True
            if i == len(str2):
                return False
            return order.find(str1[i]) < order.find(str2[i])
        for j in range(len(words) - 1):
            if compare(words[j], words[j + 1]) == False:
                return False
        return True
