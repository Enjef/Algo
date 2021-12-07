class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:  # 63.56% 57.92%
        if len(s) < 11:
            return []
        seen = set()
        out = set()
        for i in range(len(s)-9):
            if s[i:i+10] in seen:
                out.add(s[i:i+10])
            seen.add(s[i:i+10])
        return out
