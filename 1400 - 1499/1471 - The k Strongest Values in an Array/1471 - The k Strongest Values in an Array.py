class Solution:
    def getStrongest(self, arr, k):  # 50.51%  8.25%
        median = sorted(arr)[(len(arr)-1)//2]
        vals = []
        for num in arr:
            heappush(vals, (-abs(num-median), -num))
        out = []
        for _ in range(k):
            out.append(-heappop(vals)[1])
        return out

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        len_arr = len(arr)
        arr.sort()
        med = arr[(len_arr-1) // 2]
        i, j = 0, len_arr - 1
        while k>0:
            if abs(arr[i] - med) > abs(arr[j] - med):
                i += 1
            else:
                j -= 1
            k -= 1
        answer = arr[:i] + arr[j+1:]
        return answer

    def getStrongest_best_memory(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        m, X = arr[(n - 1) >> 1], []
        i, j = 0, n - 1
        while len(X) < k:
            if arr[j] - m >= m - arr[i]:
                X.append(arr[j])
                j -= 1
            else:
                X.append(arr[i])
                i += 1
        return X
