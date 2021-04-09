dict_a = {
    '(': ')',
    '[': ']',
    '{': '}',
}


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        if s[0] not in dict_a:
            return False
        temp = ''
        for i in range(len(s)):
            if s[i] in dict_a:
                temp += s[i]
                continue
            if s[i] not in dict_a:
                if not temp or s[i] != dict_a[temp[-1]]:
                    return False
                if temp and s[i] == dict_a[temp[-1]]:
                    temp = temp[:-1]
                    continue
        return temp == ''


x = Solution()
print(x.isValid(r'(('))
