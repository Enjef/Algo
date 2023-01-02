class Solution:
    # 98.80%  21.12%
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        res = 0
        if cost1 < cost2:
            cost1, cost2 = cost2, cost1
        for i in range(total//cost1+1):
            res += (total-(cost1*i))//cost2 + 1
        return res


class Solution_best_speed:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        c, C = sorted([cost1, cost2])
        blocksize = c * C
        return sum(
            (rest // c + 1) * blocks + C * comb(blocks, 2)
            for rest in range(total % C, min(blocksize, total + 1), C)
            for blocks in [(total - rest) // blocksize + 1]
        )

    def waysToBuyPensPencils_2nd(self, total: int, cost1: int, cost2: int) -> int:
        d = gcd(cost1, cost2)
        c, C = sorted([cost1 // d, cost2 // d])
        total //= d
        blocksize = c * C
        blocks, partial = divmod(total, blocksize)
        result = sum(rest // c + 1
                     for rest in range(partial, -1, -C))
        if blocks:
            blocksum = sum(rest // c + 1
                           for rest in range(total, total - blocksize, -C))
            result += blocks * blocksum - blocksize * comb(blocks, 2)
        return result


class Solution_best_memory:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        numWays = 0
        maxPens = total // cost1
        for i in range(maxPens+1):
            numWays += ((total - cost1*i) // cost2) + 1
        return numWays

    def waysToBuyPensPencils_2nd(self, total: int, cost1: int, cost2: int) -> int:
        x = 0
        ans = 0
        while (x*cost1 <= total):
            ans += int((total-x*cost1)/cost2)+1
            x += 1
        return ans
