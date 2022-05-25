class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:  # 5.31% 67.23%
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        arr = []
        for num in envelopes:
            if not arr or (arr[-1][0] < num[0] and arr[-1][1] < num[1]):
                arr.append(num)
            left, right = 0, len(arr)-1
            while left < right:
                mid = left + (right-left)//2
                if arr[mid][0] < num[0] and arr[mid][1] < num[1]:
                    left = mid + 1
                else:
                    right = mid
            arr[left] = num
        return len(arr)

    def maxEnvelopes_best_speed(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: x[0] * 1000000 - x[1])
        lis = []
        for e in envelopes:
            idx = bisect.bisect_left(lis, e[1])
            if idx == len(lis):
                lis.append(e[1])
            else:
                lis[idx] = e[1]
        return len(lis)

    def maxEnvelopes_3d_best_speed(self, envelopes: List[List[int]]) -> int:
        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))

        def lis(nums):
            dp = []
            for num in nums:
                idx = bisect_left(dp, num)
                if idx == len(dp):
                    dp.append(num)
                else:
                    dp[idx] = num
            return len(dp)
        return lis([i[1] for i in envelopes])

    def maxEnvelopes_best_memory(self, envelopes: List[List[int]]) -> int:
        def sorter(x):
            return [x[0], -x[1]]
        envelopes.sort(key=sorter)
        for i in range(len(envelopes)):
            envelopes[i] = envelopes[i][1]
        sub = [envelopes[0]]
        for height in envelopes:
            index = bisect_left(sub, height)
            if index == len(sub):
                sub.append(height)
            else:
                sub[index] = height
        return len(sub)
