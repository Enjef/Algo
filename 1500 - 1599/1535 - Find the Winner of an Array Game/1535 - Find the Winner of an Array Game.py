class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:  # 34.58% 9.02%
        if len(arr) < k:
            return max(arr)
        cur_max = arr[0]
        cur_count = 0
        arr += sorted(arr)
        for i in range(1, len(arr)):
            if cur_max > arr[i]:
                cur_count += 1
            else:
                cur_count = 1
                cur_max = arr[i]
            if cur_count == k:
                return cur_max
        return

    def getWinner_v2(self, arr: List[int], k: int) -> int:  # 24.81% 45.86%
        if len(arr) < k:
            return max(arr)
        cur_max = arr[0]
        cur_count = 0
        for i in range(1, len(arr)):
            if cur_max > arr[i]:
                cur_count += 1
            else:
                cur_count = 1
                cur_max = arr[i]
            if cur_count == k:
                return cur_max
        return cur_max

    def getWinner_best_speed(self, arr: List[int], k: int) -> int:
        if not arr or not k:
            return -1
        cur_k = 0
        cur_winner = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > cur_winner:
                cur_winner = arr[i]
                cur_k = 0
            cur_k += 1
            if cur_k == k:
                break
        return cur_winner

    def getWinner_best_memory(self, arr: List[int], k: int) -> int:
        win_count = 0
        count = 0
        while win_count != k:
            if arr[0] > arr[1]:
                win_count += 1
                arr.append(arr.pop(1))
            else:
                win_count = 1
                arr.append(arr.pop(0))
            count += 1
            if count > len(arr):
                break
        return arr[0]
