class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:  # 8.95% 50.64%
        for i in range(len(arr)):
            if arr[i] == 1:
                continue
            for j in range(i+1, len(arr)):
                if arr[i] == 0 and arr[j] == 0:
                    return True
                if arr[i] == 0 or arr[j] == 0:
                    continue
                if arr[i] == arr[j]:
                    continue
                if (arr[i] < 0 and arr[j] > 0) or (arr[i] > 0 and arr[j] < 0):
                    continue
                if arr[j] == 1:
                    continue
                if arr[i] / arr[j] == 2 or arr[j] / arr[i] == 2:
                    return True
        return False

    def checkIfExist_set(self, arr: List[int]) -> bool:  # 96.86% 91.74%
        x_set = set()
        for i in arr:
            if i / 2 in x_set or i * 2 in x_set:
                return True
            x_set.add(i)
        return False

    def checkIfExist_study_plan(self, arr: List[int]) -> bool:  # 81.52% 17.40%
        n = len(arr)
        arr.sort()
        for i, num in enumerate(arr):
            left, right = 0, n-1
            target = 2*num
            while left <= right:
                mid = left + (right-left)//2
                if mid != i and arr[mid] == target:
                    return True
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

    def checkIfExist_best_speed(self, arr: List[int]) -> bool:
        cnt_dict = dict()
        for x in arr:
            cnt_dict[x] = cnt_dict[x] + 1 if x in cnt_dict else 1
        for x in arr:
            if x * 2 in cnt_dict:
                if x != 0 or cnt_dict[0] >= 2:
                    return True
        return False
