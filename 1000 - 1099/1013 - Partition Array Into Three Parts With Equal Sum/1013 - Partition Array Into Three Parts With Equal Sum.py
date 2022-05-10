class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:  # 73.41% 83.71%
        target = sum(arr) / 3
        cur = 0
        out = 0
        for num in arr:
            cur += num
            if cur == target:
                cur = 0
                out += 1
        return out >= 3

    def canThreePartsEqualSum_best_speed(self, arr: List[int]) -> bool:
        c=0
        s=sum(arr)
        s1=s//3
        s2=0
        if s%3 !=0 :
            return False
        for i in arr:
            s2+=i
            if s2==s1:
                s2=0
                c+=1
        return c>=3

    def canThreePartsEqualSum_2nd_best_speed(self, arr: List[int]) -> bool:
        total = sum(arr)
        remainder = total%3
        if remainder > 0:
            return False
        target = total/3
        currentSum = 0
        count = 2
        for i, num in enumerate(arr):
            currentSum += num
            if currentSum == target:
                count -= 1
                currentSum = 0
            if count == 0 and i != (len(arr) - 1):
                return True
        return False

    def canThreePartsEqualSum_best_memory(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        target = total // 3
        cur = 0
        for i, num in enumerate(arr):
            cur += num
            arr[i] = cur
        tasks = [target * i for i in range(1, 4)]
        if arr.pop() != tasks.pop():
            return False
        while tasks and arr:
            if tasks[-1] == arr.pop():
                tasks.pop()
        return len(tasks) == 0
