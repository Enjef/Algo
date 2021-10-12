class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        d = 'abcdefghijklmnopqrstuvwxyz'
        def helper(word):
            score = 0
            for letter in word:
                score = score*10 + d.index(letter)
            return score
        return helper(firstWord) + helper(secondWord) == helper(targetWord)

    def isSumEqual_1(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        letter = {
            "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6,
            "h": 7, "i": 8, "j": 9
        }
        words = {f'{firstWord}': 0, f'{secondWord}': 0, f'{targetWord}': 0}
        for item in words:
            for char in item:
                words[item] *= 10
                words[item] += letter[char]
        return(words[
            f'{firstWord}'] + words[f'{secondWord}'] == words[f'{targetWord}'])
