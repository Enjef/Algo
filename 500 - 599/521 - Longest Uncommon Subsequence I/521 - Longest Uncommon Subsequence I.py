class Solution:
    def findLUSlength(self, a: str, b: str) -> int:  # 66.11% 43.36%
        if a == b:
            return -1
        return len(a) if len(a) > len(b) else len(b)

    def findLUSlength_short(self, a: str, b: str) -> int:  # 97.87% 43.36%
        return max(len(a), len(b)) if a != b else -1
