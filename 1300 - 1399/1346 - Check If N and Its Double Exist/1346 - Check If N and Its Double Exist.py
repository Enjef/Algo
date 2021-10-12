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
