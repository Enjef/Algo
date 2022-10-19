class Solution:
    # 20.98% 96.82% (86.07% 64.63%)
    def minimumRecolors(self, blocks: str, k: int) -> int:
        if 'B'*k in blocks:
            return 0
        n = len(blocks)
        res = cur = sum([blocks[i] != 'B' for i in range(k)])
        for i in range(k, n):
            cur += (blocks[i] != 'B') - (blocks[i-k] != 'B')
            res = min(res, cur)
        return res


class Solution_best_speed:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white_block_count = 0
        for i in range(k):
            if blocks[i] == 'W':
                white_block_count += 1
        min_white_block_count = white_block_count
        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                white_block_count += 1
            if blocks[i-k] == 'W':
                white_block_count -= 1
            if white_block_count < min_white_block_count:
                min_white_block_count = white_block_count
        return min_white_block_count


class Solution_best_memory:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        prefix = [0]
        count = 0
        for b in blocks:
            if b == 'W':
                count += 1
            prefix.append(count)
        n = len(prefix)
        ans = float('inf')
        for i in range(k, n):
            ans = min(ans, prefix[i]-prefix[i-k])
        return ans
