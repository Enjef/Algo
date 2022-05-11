class Solution:
    def countVowelStrings(self, n: int) -> int:  # 5.08% 65.31%
        def dfs(idx, cur):
            if len(cur) == n:
                self.out += 1
                return
            for i in range(idx, len(vowels)):
                dfs(i, cur+vowels[i])
            return

        vowels = ['a', 'e', 'i', 'o', 'u']
        self.out = 0
        dfs(0, '')
        return self.out

    def countVowelStrings_best_speed(self, n: int) -> int:
        matrix = []
        for i in range(n):
            matrix.append([0]*5)
        matrix[0] = [1, 2, 3, 4, 5]
        for i in range(1, n):
            for j in range(5):
                if j == 0:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        print(matrix)
        return matrix[-1][-1]

    def countVowelStrings_2nd_best_speed(self, n: int) -> int:
        vowels = 5
        size = n
        memo = [[None for _ in range(size)] for _ in range(vowels)]

        def rec(i, n):
            if i == vowels-1:
                return 1
            if n >= size:
                return 1
            if memo[i][n] != None:
                return memo[i][n]
            using = rec(i, n+1)
            not_using = rec(i+1, n)
            memo[i][n] = using + not_using
            return memo[i][n]

        return rec(0, 0)

    def countVowelStrings_3d_best_speed(self, n: int) -> int:
        return (n+4)*(n+3)*(n+2)*(n+1) // 24

    def countVowelStrings_4th_best_speed(self, n: int) -> int:
        def nCr(n, r):
            if n-r < r:
                return nCr(n, n-r)
            c = 1
            for k in range(1, r+1):
                c *= n-k+1
                c //= k
            return c

        return nCr(n+4, 4)

    def countVowelStrings_best_memory(self, n: int) -> int:
        lst = [5, 4, 3, 2, 1]
        if n == 1:
            return 5
        if n == 2:
            return 15
        for i in range(3, n+1):
            lst = [
                sum(lst), sum(lst[1:]), sum(lst[2:]),
                sum(lst[3:]), sum(lst[4:])
            ]
        return sum(lst)

    def countVowelStrings_2nd_best_memory(self, n: int) -> int:
        sums = [1 for _ in range(5)]
        for _ in range(n):
            for i in range(3, -1, -1):
                sums[i] += sums[i+1]
        return sums[0]

    def countVowelStrings_3d_best_speed(self, n: int) -> int:
        table: list[int] = [1] * 5
        for _ in range(n):
            for j in range(3, -1, -1):
                table[j] += table[j + 1]
        return table[0]
