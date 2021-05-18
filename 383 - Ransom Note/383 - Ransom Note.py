class Solution:
    def canConstruct(self, ransomNote, magazine):
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
