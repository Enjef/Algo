class Solution:
    def totalNQueens(self, n: int) -> int:  # 96.48% 39.44%
        def helper(cols, diags, rdiags, row):
            if row == n:
                return 1
            result = 0
            for col in range(n):
                rdiag, diag = row-col, col+row
                if col in cols or rdiag in rdiags or diag in diags:
                    continue
                cols.add(col)
                diags.add(diag)
                rdiags.add(rdiag)
                result += helper(cols, diags, rdiags, row+1)
                cols.discard(col)
                diags.discard(diag)
                rdiags.discard(rdiag)
            return result

        diags = set()
        rdiags = set()
        cols = set()
        return helper(cols, diags, rdiags, 0)

    def totalNQueens_v2(self, n: int) -> int:  # 77.11% 99.25%
        def helper(row=0):
            if row == n:
                self.result += 1
                return
            for col in range(n):
                rdiag, diag = row-col, col+row
                if col in cols or rdiag in rdiags or diag in diags:
                    continue
                cols.add(col)
                diags.add(diag)
                rdiags.add(rdiag)
                helper(row+1)
                cols.discard(col)
                diags.discard(diag)
                rdiags.discard(rdiag)
            return

        diags = set()
        rdiags = set()
        cols = set()
        self.result = 0
        helper()
        return self.result

    def totalNQueens_v3(self, n: int) -> int:  # 74.90% 80.48%
        def adder(sets, elements):
            for seen, el in zip(sets, elements):
                seen.add(el)
            return
            
        def discader(sets, elements):
            for seen, el in zip(sets, elements):
                seen.discard(el)
            return
        
        def helper(row=0):
            if row == n:
                self.result += 1
                return
            for col in range(n):
                rdiag, diag = row-col, col+row
                if col in cols or rdiag in rdiags or diag in diags:
                    continue
                adder([cols, diags, rdiags], [col, diag, rdiag])
                helper(row+1)
                discader([cols, diags, rdiags], [col, diag, rdiag])
            return

        diags = set()
        rdiags = set()
        cols = set()
        self.result = 0
        helper()
        return self.result

    def totalNQueens_v4(self, n: int) -> int:  # 66.30%
        def helper(row=0):
            if row == n:
                self.result += 1
                return
            for col in range(n):
                rdiag, diag = row-col, col+row
                if col in cols or rdiag in rdiags or diag in diags:
                    continue
                [x.add(y) for x, y in zip([cols, diags, rdiags], [col, diag, rdiag])]
                helper(row+1)
                [x.discard(y) for x, y in zip([cols, diags, rdiags], [col, diag, rdiag])]
            return

        diags = set()
        rdiags = set()
        cols = set()
        self.result = 0
        helper()
        return self.result

    def totalNQueens_v5(self, n, diags=set(), rdiags=set(), cols=set(), row=0) -> int:  # 41.40% 15.44% (60.21% 80.48%)
        if row == n:
            return 1
        result = 0
        for col in range(n):
            rdiag, diag = row-col, col+row
            if col in cols or rdiag in rdiags or diag in diags:
                continue
            [x.add(y) for x, y in zip([cols, diags, rdiags], [col, diag, rdiag])]
            result += self.totalNQueens(n, diags, rdiags, cols, row+1)
            [x.discard(y) for x, y in zip([cols, diags, rdiags], [col, diag, rdiag])]
        return result

    def totalNQueens_best_memory(self, n: int) -> int:
        result = 0
        numDiags = (n * 2) - 1
        columns = [False] * n
        leftDiag = [False] * numDiags
        rightDiag = [False] * numDiags

        def bt(row: int):
            nonlocal result
            if row == n:
                result += 1
                return
            for col in range(n):
                ldIdx = row + col
                rdIdx = (n - row - 1) + col
                if columns[col] or leftDiag[ldIdx] or rightDiag[rdIdx]:
                    continue
                columns[col] = True
                leftDiag[ldIdx] = True
                rightDiag[rdIdx] = True
                bt(row + 1)
                columns[col] = False
                leftDiag[ldIdx] = False
                rightDiag[rdIdx] = False
        bt(0)
        return result
