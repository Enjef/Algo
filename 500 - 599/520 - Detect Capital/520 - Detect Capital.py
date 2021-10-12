class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        if word.islower():
            return True
        if word[0].isupper():
            if word[1:].isupper():
                return True
            if word[1:].islower():
                return True
        return False
