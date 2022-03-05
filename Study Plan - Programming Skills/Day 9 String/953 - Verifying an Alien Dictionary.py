class Solution:
    def isAlienSorted(self, words, order):  # 60.86% 50.06%
        def custom_weight(word):
            return [weight[x] for x in word]
        
        weight = {char: idx for idx, char in enumerate(order)}
        return words == sorted(words, key=custom_weight)
