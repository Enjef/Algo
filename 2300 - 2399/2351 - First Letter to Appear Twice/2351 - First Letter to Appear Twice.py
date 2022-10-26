class Solution:
    # 5.21% 7.83% (24.59% 94.31%)
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for char in s:
            if char in seen:
                return char
            seen.add(char)
        return
