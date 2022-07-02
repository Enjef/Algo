class Solution:
    #  43.13% 65.76%
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        for char in s:
            count[char] += 1
        any_odd = 0
        result = 0
        for num in count.values():
            result += num - num % 2
            if num % 2:
                any_odd = 1
        return result + any_odd
