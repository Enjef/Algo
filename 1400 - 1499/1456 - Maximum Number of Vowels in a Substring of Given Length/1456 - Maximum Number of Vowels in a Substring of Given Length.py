class Solution:
    def maxVowels(self, s: str, k: int) -> int:  # 46.15% 99.78%
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        cur_len = 0
        for i in range(k):
            if s[i] in vowels:
                cur_len += 1 
        result = cur_len
        for i in range(k, len(s)):
            if s[i-k] in vowels:
                cur_len -= 1
            if s[i] in vowels:
                cur_len += 1
            result = max(result, cur_len)
        return result

    def maxVowels_2nd_best_speed(self, s: str, k: int) -> int:
        vowels = [0]
        cumulative = 0
        for char in s:
            if char in "aeiou":
                cumulative += 1
            vowels.append(cumulative)
        return max(
            (right - left for left, right in zip(vowels, vowels[k:])), default=0)

    def maxVowels_best_memory(self, s: str, k: int) -> int:
        vowels = Counter({v: 0 for v in 'aeiou'})
        i = maxCount = currCount = 0
        for j in range(len(s)):
            if s[j] in vowels:
                currCount += 1
            if j-i+1 > k:
                if s[i] in vowels:
                    currCount -= 1
                i += 1
            if j-i+1 == k:
                maxCount = max(maxCount, currCount)
            if currCount == k:
                return k
        return maxCount
