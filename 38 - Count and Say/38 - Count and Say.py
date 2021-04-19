class Solution:
    def countAndSay(self, n: int) -> str:
        d_str = '1'
        if n == 1:
            return d_str
        d_str += d_str
        if n == 2:
            return d_str
        while n - 2 > 0:
            check = d_str[0]
            count = 1
            temp = ''
            for char in range(1, len(d_str)):
                if d_str[char] == check:
                    count += 1
                else:
                    temp += str(count) + check
                    check = d_str[char]
                    count = 1
            temp += str(count) + check
            n -= 1
            d_str = temp
        return d_str


s = '123'
print(s[0]+s[2]+str(5))
x = Solution()
print(x.countAndSay(4))

