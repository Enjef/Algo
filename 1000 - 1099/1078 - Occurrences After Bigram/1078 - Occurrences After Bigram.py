class Solution:
    def findOcurrences(
            self,
            text: str,
            first: str,
            second: str) -> List[str]:  # 77.61% 22.88%
        out = []
        words = text.split()
        for i in range(2, len(words)):
            if words[i-2] == first and words[i-1] == second:
                out.append(words[i])
        return out
