class Solution:
    def areNumbersAscending(self, s: str) -> bool: # 97.93% 75.70%
        arr = [int(x) for x in s.split() if x.isdigit()]
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]:
                return False
        return True

    def areNumbersAscending_best_memory(self, s: str) -> bool:
        slist = s.split(' ')
        num = 0
        for a in slist:
            if a.isnumeric():
                if int(a) > num:
                    num = int(a)
                else:
                     return False
        return True
