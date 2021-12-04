class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0:
            return False
        i = 0
        j = int(math.log10(x))
        while i < j:
            if x // 10 ** j % 10 != x // 10 ** i % 10:
                return False
            i += 1
            j -= 1
        return True

    def isPalindrome_best_speed(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

    def isPalindrome_7th_best_speed(self, x: int) -> bool:
        if x < 0:
            return False
        number = x
        reverse = 0
        while number:
            reverse = reverse * 10 + number % 10
            number //= 10
        return x == reverse
