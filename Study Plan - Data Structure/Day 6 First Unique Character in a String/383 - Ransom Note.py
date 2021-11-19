class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:  # 25.59%
        note = list(ransomNote)
        mag = list(magazine)
        while note:
            cur = note.pop()
            if cur in mag:
                mag.remove(cur)
            else:
                return False
        return True

    def canConstruct_v2(
            self,
            ransomNote: str,
            magazine: str) -> bool:  # 28.88% 64.11%
        count = {}
        for char in magazine:
            count[char] = count.get(char, 0) + 1
        for char in ransomNote:
            if char not in count or count[char] < 1:
                return False
            else:
                count[char] -= 1
        return True
