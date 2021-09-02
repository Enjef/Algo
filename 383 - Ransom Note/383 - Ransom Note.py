class Solution:
    def canConstruct(self, ransomNote, magazine):  # 23.31% 11.67%
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_note = list(ransomNote)
        magazine = list(magazine)
        for i in range(len(ransom_note)):
            if ransom_note[i] in magazine:
                magazine.remove(ransom_note[i])
            else:
                return False
        return True

    def canConstruct_sp_day_6(
            self,
            ransomNote: str,
            magazine: str) -> bool:  # 22.98% 11.67%
        note = list(ransomNote)
        mag = list(magazine)
        while note:
            cur = note.pop()
            if cur in mag:
                mag.remove(cur)
            else:
                return False
        return True

    def canConstruct_best_speed(self, ransomNote, magazine):
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True
