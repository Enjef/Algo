class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:  # 5.21% 10.85%
        anagram = sorted(p)
        out = []
        temp = ''
        for i, char in enumerate(s):
            temp += char
            if len(temp) == len(anagram):
                if sorted(temp) == anagram:
                    out.append(i-len(temp)+1)
                temp = temp[1:]
        return out

    def findAnagrams_stop(self, s: str, p: str) -> List[int]:  # 13.00% 99.03%
        anagram = sorted(p)
        check = set(anagram)
        out = []
        temp = ''
        for i, char in enumerate(s):
            if char not in check:
                temp = ''
                continue
            temp += char
            if len(temp) == len(anagram):
                if sorted(temp) == anagram:
                    out.append(i-len(temp)+1)
                temp = temp[1:]
        return out
