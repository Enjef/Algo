class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note = list(ransomNote)
        mag = list(magazine)
        while note:
            cur = note.pop()
            if cur in mag:
                mag.remove(cur)
            else:
                return False
        return True
