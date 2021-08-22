class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:  # 72.90% 64.27%
        if k == 0:
            return [0] * len(code)
        code_old = code * 3
        if k > 0:
            for i in range(len(code)):
                code[i] = sum(code_old[len(code)+i+1:len(code)+i+k+1])
        else:
            for i in range(len(code)):
                code[i] = sum(code_old[len(code)+i+k:len(code)+i])
        return code

    def decrypt_flat(
            self,
            code: List[int],
            k: int) -> List[int]:  # (72.90% 64.27%) (100.00 % 34.05 %)
        if k == 0:
            return [0] * len(code)
        code_old = code * 3
        if k > 0:
            left = 1
            right = k + 1
        else:
            left = k
            right = 0
        for i in range(len(code)):
            code[i] = sum(code_old[len(code)+i+left: len(code)+i+right])
        return code

    def decrypt_best(self, code: List[int], k: int) -> List[int]:  # 88.01% 8%
        if k == 0:
            return [0] * len(code)
        if k < 0:
            return self.decrypt_best(code[::-1], -k)[::-1]
        a = code[:]
        a += a
        for i in range(len(a)-2, -1, -1):
            a[i] += a[i+1]
        ans = [0]*len(code)
        for i in range(len(ans)):
            ans[i] = a[i+1]-a[i+k+1]
        return ans
