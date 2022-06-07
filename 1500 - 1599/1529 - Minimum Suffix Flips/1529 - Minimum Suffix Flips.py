class Solution:
    def minFlips(self, target: str) -> int:  # 86.60% 60.31%
        n = len(target)
        count = 0
        for i in range(n):
            if target[i] == '0':
                if count % 2:
                    count += 1
            else:
                if not count % 2:
                    count += 1
        return count

    def minFlips_best_spee(self, target: str) -> int:
        return target.count('10')*2 + (target[-1] == '1')

    def minFlips_3d_best_speed(self, target: str) -> int:
        flips = 0
        status = '0'
        for c in target:
            if c != status:
                flips += 1
                status = '0' if status == '1' else '1'
        return flips

    def minFlips_best_memory(self, target: str) -> int:
        if target.count('1') == 0:
            return 0
        count = 1
        n = len(target)
        for i in range(n-1):
            if target[n-i-2] != target[n-i-1]:
                count += 1
        return count if target[0] == '1' else count-1
