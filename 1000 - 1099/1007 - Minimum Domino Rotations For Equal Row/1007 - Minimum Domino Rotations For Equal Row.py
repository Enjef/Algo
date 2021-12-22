class Solution:
    def minDominoRotations_mock(
            self, tops: List[int], bottoms: List[int]) -> int:  # 50.00% 59.66%
        def helper(fix, rotate, target):
            count = 0
            for i in range(len(fix)):
                if fix[i] == target:
                    continue
                if rotate[i] != target:
                    count = float('inf')
                    break
                count += 1
            return count

        out = []
        top_count = dict(zip(list(range(1, 7)), [0]*6))
        bot_count = dict(zip(list(range(1, 7)), [0]*6))
        for num in tops:
            top_count[num] += 1
        for num in bottoms:
            bot_count[num] += 1
        posible = []
        for num in range(1, 7):
            if top_count[num] + bot_count[num] >= len(tops):
                posible.append(num)
        for num in posible:
            if top_count[num] < bot_count[num]:
                out.append(helper(bottoms, tops, num))
            else:
                out.append(helper(tops, bottoms, num))
        if not out or min(out) == float('inf'):
            return -1
        return min(out)

    def containsAll(self, tops, bottoms, num):
        for t, b in zip(tops, bottoms):
            if t != num and b != num:
                return False
        return True

    def minDominoRotations_best_speed(
            self, tops: List[int], bottoms: List[int]) -> int:
        nums = list()
        if self.containsAll(tops, bottoms, tops[0]):
            nums.append(tops[0])
        if self.containsAll(tops, bottoms, bottoms[0]):
            nums.append(bottoms[0])
        if len(nums) == 0:
            return -1
        ans = float('inf')
        n = len(tops)
        for num in nums:
            ans = min(n - tops.count(num), ans)
            ans = min(n - bottoms.count(num), ans)
        return ans

    from collections import Counter

    def minDominoRotations_2nd_best_speed(
            self, A: List[int], B: List[int]) -> int:
        for x in [A[0], B[0]]:
            if all(x in d for d in zip(A, B)):
                return len(A) - max(A.count(x), B.count(x))
        return -1

    def minDominoRotations_3d_best_speed(
            self, A: List[int], B: List[int]) -> int:
        solutions = [A[0],  B[0]]
        l = len(A)
        swapA = 0
        swapB = 0
        flag = 0
        for i in solutions:
            swapA = 0
            swapB = 0
            flag = 0
            for j in range(l):
                if A[j] == B[j] == i:
                    continue
                elif A[j] == i:
                    swapB += 1
                elif B[j] == i:
                    swapA += 1
                else:
                    flag = 1
                    break
            print(swapA, swapB)
            if flag == 0:
                return min(swapA, swapB)
        return -1

    def minDominoRotations_best_memory(
            self, tops: List[int], bottoms: List[int]) -> int:
        def check(num):
            top_rotations = bottom_rotations = 0
            
            for top, bottom in zip(tops, bottoms):
                if top != num and bottom != num:
                    return -1
                elif top != num:
                    top_rotations += 1
                elif bottom != num:
                    bottom_rotations += 1
            return min(top_rotations, bottom_rotations)
        rotations = {check(tops[0]), check(bottoms[0])}
        if rotations == {-1}:
            return -1
        if -1 in rotations:
            rotations.remove(-1)
        return min(rotations)

    def minDominoRotations_2nd_best_memory(
            self, A: List[int], B: List[int]) -> int:
        def check(x):
            rotations_a = rotations_b = 0
            for i in range(n):
                if A[i] != x and B[i] != x: 
                    return -1
                elif A[i] != x: 
                    rotations_a += 1
                elif B[i] != x: 
                    rotations_b += 1
            return min(rotations_a, rotations_b)
        n = len(A)
        rotations = check(A[0]) 
        if rotations != -1 or A[0] == B[0]: 
            return rotations 
        else: 
            return check(B[0])
