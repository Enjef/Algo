class Solution:
    def numTilePossibilities(self, tiles: str) -> int:  # 44.55% 11.58%
        def perm(arr, cur='', out=set()):
            for i in range(len(arr)):
                out.add(cur+arr[i])
                perm(arr[:i]+arr[i+1:], cur+arr[i], out)
            return len(out)
        return perm(tiles)

    def numTilePossibilities_top_5_speed(self, tiles: str) -> int:
        ans = 0
        for i in range(1, len(tiles) + 1):
            ans += len(set(permutations(tiles, i)))
        return ans

    def numTilePossibilities_best_memory(self, tiles: str) -> int:
        res = 0
        counts = defaultdict(lambda: 0)
        for tile in tiles:
            counts[ord(tile) - ord('A')] += 1

        def dfs():
            nonlocal res, counts
            for c in counts:
                if counts[c] == 0:
                    continue
                res += 1
                counts[c] -= 1
                dfs()
                counts[c] += 1
        dfs()
        return res
