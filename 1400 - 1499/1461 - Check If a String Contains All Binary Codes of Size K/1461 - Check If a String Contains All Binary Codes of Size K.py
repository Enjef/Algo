class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:  # 5.31% 5.31%
        test = set(
            [bin(x)[2:] for x in range(int('1'+'0'*(k-1), 2), int('1'*k, 2)+1)])
        test.add('0'*k)
        n = len(s)
        for i in range(n-k+1):
            test.discard(s[i:i+k])
        return not test

    def hasAllCodes_best_speed(self, s: str, k: int) -> bool:
        need = 2 ** k
        got = set()
        temp = ''
        for i in range(k, len(s)+1):
            temp = s[i-k:i]
            if temp not in got:
                got.add(temp)
                need -= 1
            if need == 0:
                return True
        return False

    def hasAllCodes_best_memory(self, s: str, k: int) -> bool:
        if len(s) < (k - 1) + 2 ** k:
            return False
        curr_num = 0
        for i in range(k):
            curr_num = (curr_num << 1) + int(s[i])
        codes = {curr_num}
        for i in range(k, len(s)):
            curr_num = (curr_num << 1) + int(s[i])
            if s[i - k] == '1':
                curr_num -= (1 << k)
            codes.add(curr_num)
        return len(codes) == 2 ** k
