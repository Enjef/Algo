class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)  # 75.96% 84.20%
        avg = sum(arr[:k])/k
        res = 0 if avg < threshold else 1
        j = 0
        for i in range(k, n):
            avg += (arr[i]-avg)/k-(arr[j]-avg)/k
            res += 0 if avg < threshold else 1
            j += 1
        return res

    def numOfSubarrays_best_speed(self, arr, k, threshold):
        count = 0
        current = sum(arr[0:k])
        if current/k >= threshold:
            count += 1
        for x in range(k, len(arr)):
            current += arr[x] - arr[x-k]
            if current/k >= threshold:
                count += 1
        return count
