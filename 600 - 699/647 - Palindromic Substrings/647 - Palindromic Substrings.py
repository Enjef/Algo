class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        table = [[False] * n for _ in range(n)]
        count = 0
        for i in range(n):
            table[i][i] = True
            count += 1
        for i in range(n-1):
            if s[i] == s[i+1]:
                table[i][i+1] = True
                count += 1
        for k in range(3, n+1):
            for i in range(n-k+1):
                j = i+k-1
                if table[i+1][j-1] and s[i] == s[j]:
                    table[i][j] = True
                    count += 1
        return count


    def countSubstrings_best_speed(self, s: str) -> int:
            l, r = 0, 0
            num_palindromes = 0
            while r < len(s):
                while r < len(s) and s[r] == s[l]:
                    r += 1
                num_palindromes += ((r-l)*(r-l+1))//2
                j = l-1
                k = r
                while j >= 0 and k < len(s) and s[j] == s[k]:
                    num_palindromes += 1
                    j -= 1
                    k += 1
                l = r
            return num_palindromes

    def countSubstrings_best_memory(self, s: str) -> int:
        cnt = 0
        l = len(s)
        for i in range(l):
            j = 0
            while i - j >= 0 and i + j < l and s[i-j] == s[i+j]:
                cnt += 1
                j += 1
        for i in range(l-1):
            j = 0
            while i - j >= 0 and i + j + 1 < l and s[i-j] == s[i+j+1]:
                cnt += 1
                j += 1
        return cnt
