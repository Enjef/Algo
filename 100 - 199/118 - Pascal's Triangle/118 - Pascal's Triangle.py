class Solution(object):
    def generate(self, numRows):  # 76.84% 36.14%
        out = [[1]]
        cur = []
        if numRows == 1:
            return out
        out.append([1, 1])
        if numRows == 2:
            return out
        for i in range(2, numRows):
            cur = (i+1) * [1]
            for j in range(1, len(cur) - 1):
                cur[j] = out[-1][j-1] + out[-1][j]
            out.append(cur)
        return out

    def generate_study_plan_day_4(
            self,
            numRows: int) -> List[List[int]]:  # 11.10% 81.74%
        out = [[1], [1, 1]]
        if numRows == 1:
            return [out[0]]
        for _ in range(numRows-2):
            out.append([1])
            for j in range(1, len(out[-2])):
                out[-1].append(out[-2][j-1] + out[-2][j])
            out[-1].append(1)
        return out

    def generate_best_speed(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = [[1]*i for i in range(1, numRows+1)]
        for i in range(2, numRows):
            for j in range(1, len(triangle[i])-1):
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
        return triangle
