class Solution:
    def sumZero(self, n: int) -> List[int]:  # 81.20% 91.44%
        out = []
        if n % 2 != 0:
            out.append(0)
        for i in range(1, n//2+1):
            out.append(i)
            out.append(-i)
        return out

    def sumZero_best_speed(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n % 2 == 0:
            output = []
            for i in range(1, n//2+1):
                output.extend([i, -i])
            return output
        else:
            output = [0]
            for i in range(1, n//2+1):
                output.extend([i, -i])
            return output
