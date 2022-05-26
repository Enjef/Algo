class Solution:
    def largestGoodInteger(self, num: str) -> str:  # 84.70% 24.45%
        cur = ''
        result = ''
        for char in num:
            if not cur or cur and cur[-1] == char:
                cur += char
            elif cur and cur[-1] != char:
                if len(cur) >= 3:
                    result = max(result, cur[:3])
                cur = char
        if len(cur) >= 3:
            result = max(result, cur[:3])
        return result

    def largestGoodInteger_best_speed(self, num: str) -> str:
        for i in range(9, -1, -1):
            compare = str(i) * 3
            if compare in num:
                return compare
        return ''

    def largestGoodInteger_2nd_best_speed(self, num: str) -> str:
        ans = ''
        q = ''
        for char in num:
            if q == '':
                q += char
            else:
                if char == q[-1]:
                    q += char
                else:
                    q = char
                if q == 3*q[0]:
                    if ans == '':
                        ans = q
                    else:
                        if int(q) > int(ans):
                            ans = q
        return ans

    def largestGoodInteger_best_memory(self, num: str) -> str:
        integer = ''
        for i in range(1, len(num)-1):
            if num[i-1] == num[i] == num[i+1]:
                integer = max(integer, num[i])
        return 3 * integer
