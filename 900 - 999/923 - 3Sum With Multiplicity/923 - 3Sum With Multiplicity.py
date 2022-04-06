class Solution:
    def threeSumMulti(self, arr, target):  # 40.70% 100.00%
        total = 0
        mod = 10 ** 9 + 7
        ones = defaultdict(int)
        twos = defaultdict(int)
        for t, v in enumerate(arr):
            total = total + twos[target - v]
            for k, c in ones.items():
                twos[k+v] += c
            ones[v] += 1
        return total % mod

    def threeSumMulti_best_speed(self, A: List[int], target: int) -> int:
        MOD = 1_000_000_007
        seen = Counter(A)
        A = list(set(A))
        A.sort()
        n = len(A)
        ans = 0
        for i in range(n):
            need = target - A[i]
            obs = set()
            for x in A[i:]:
                obs.add(need - x)
                if x > need:
                    break
                if x in obs:
                    a, b, c = sorted([A[i], x, need - x])
                    if a < b < c:
                        ans += seen[a] * seen[b] * seen[c]
                    if a == b < c:
                        ans += seen[a] * (seen[a] - 1) * seen[c] // 2
                    if a < b == c:
                        ans += seen[a] * seen[b] * (seen[b] - 1) // 2
                    if a == b == c:
                        ans += seen[a] * (seen[a] - 1) * (seen[a] - 2) // 6
                    ans %= MOD
        return ans

    def threeSumMulti_best_memory(self, arr: List[int], target: int) -> int:
        ans, n, mod = 0, len(arr), 10**9+7
        arr.sort()
        for i, num in enumerate(arr):
            j, k = i+1, n-1
            while j < k:
                sumjk = arr[j] + arr[k]
                if num + sumjk < target:
                    j += 1
                elif num + sumjk > target:
                    k -= 1
                else:
                    if arr[j] == arr[k]:
                        ans = (ans + (k-j+1)*(k-j)//2)%mod
                        break
                    else:
                        left, right = 1, 1
                        while j < k and arr[j] == arr[j+1]:
                            j += 1
                            left += 1
                        while j < k and arr[k-1] == arr[k]:
                            k -= 1
                            right += 1
                        ans = (ans + left*right) % mod
                        j += 1
                        k -= 1
        return ans
