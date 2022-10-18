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

    # 54.61% 7.99% (72.96% 7.99%)
    def countAndSay_daily(self, n: int) -> str:
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        step = ['1', '1']
        while n-2:
            m = len(step)
            count = 1
            new = []
            for i in range(1, m):
                if step[i] == step[i-1]:
                    count += 1
                else:
                    new.extend([str(count), step[i-1]])
                    count = 1
            new.extend([str(count), step[-1]])
            n -= 1
            step = new
        return ''.join(step)


class Solution_best_speed:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        str1 = self.countAndSay(n-1)
        ans = ''
        ch = str1[0]
        count = 1
        for i in range(1, len(str1)):
            if ch != str1[i]:
                ans += str(count)+ch
                ch = str1[i]
                count = 1
            else:
                count += 1
        ans += str(count) + ch
        return ans
