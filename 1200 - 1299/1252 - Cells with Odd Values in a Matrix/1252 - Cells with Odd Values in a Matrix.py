class Solution(object):
    def oddCells(self, m, n, indices):  # 7.97% 28.99%
        out = 0
        for i in range(m):
            for j in range(n):
                temp = 0
                for row, col in indices:
                    if row == i:
                        temp += 1
                    if col == j:
                        temp += 1
                if temp % 2 != 0:
                    out += 1
        return out

    def oddCells_best(self, m, n, ind):
        a = [0]*m
        for i in range(len(ind)):
            a[ind[i][0]] = (a[ind[i][0]]+1) % 2
        b = [0]*n
        for i in range(len(ind)):
            b[ind[i][1]] = (b[ind[i][1]]+1) % 2
        return (m-sum(a))*sum(b)+(n-sum(b))*sum(a)
