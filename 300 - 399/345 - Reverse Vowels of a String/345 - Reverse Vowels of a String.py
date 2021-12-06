class Solution:
    def reverseVowels(self, s):  # 63.82% 37.14%
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aeiou'
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and lower(s[i]) not in vowels:
                i += 1
            while i < j and lower(s[j]) not in vowels:
                j -= 1
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return "".join(s)

    def reverseVowels_mock(self, s: str) -> str:  # 95.07% 49.15%
        vowels = set('aeiouAEIOU')
        chars = list(s)
        left, right = 0, len(s) - 1
        while left <= right:
            if chars[left] not in vowels and chars[right] not in vowels:
                left += 1
                right -= 1
            elif chars[left] in vowels and chars[right] in vowels:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
            elif chars[left] in vowels:
                right -= 1
            else:
                left += 1
        return ''.join(chars)

    def reverseVowels_best_speed(self, s: str) -> str:
        s = list(s)
        l = 0
        r = len(s) - 1
        while l < r:
            while l < len(s) and s[l] not in "aeiouAEIOU":
                l += 1
            while r > 0 and s[r] not in "aeiouAEIOU":
                r -= 1  
            if l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return ''.join(s)

    def reverseVowels_best_memory(self, s: str) -> str:
        vowelList = ("a", "e", "i", "o", "u")
        vowelSeen = []
        for letter in s:
            if letter.lower() in vowelList:
                vowelSeen.append(letter)
        if len(vowelSeen) == 0:
            return s
        else:
            output = ""
            for letter in s:
                if letter.lower() in vowelList:
                    output = output + vowelSeen.pop()
                else:
                    output = output + letter
        return output
