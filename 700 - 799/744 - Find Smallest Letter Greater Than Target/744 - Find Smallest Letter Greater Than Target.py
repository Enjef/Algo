class Solution:
    def nextGreatestLetter(self, letters, target):  # 83.00% 24.34%
        n = len(letters)
        left = 0
        right = n-1
        while left < right:
            mid = left + (right-left)//2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        if left == n-1 and letters[left] <= target:
            return letters[0]
        return letters[right]

    def nextGreatestLetter_best_speed(self, letters, target):
        if letters[-1] <= target:
            return letters[0]
        else:
            for x in letters:
                if x > target:
                    return x
                else:
                    pass

    def nextGreatestLetter_2nd_best(self, letters, target):
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]

    def nextGreatestLetter_3d_best_speed(self, letters, target):
        left = 0
        right = len(letters)-1
        if (target < letters[left] or target >= letters[right]):
            return letters[left]
        while(left <= right):
            mid = (left+right)//2
            if(target < letters[mid]):
                right = mid-1
            else:
                left = mid+1
        return letters[left]
