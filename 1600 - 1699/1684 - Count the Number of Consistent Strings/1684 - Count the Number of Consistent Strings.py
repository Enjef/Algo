class Solution:
    def countConsistentStrings_my(self, allowed: str, words: List[str]) -> int:
        return len([word for word in words if not set(word) - set(allowed)])

    def countConsistentStrings_best(self, allowed, words):
        allowed = set(allowed)
        count = 0
        for word in words:
            for letter in word:
                if letter not in allowed:
                    count += 1
                    break
        return len(words) - count
