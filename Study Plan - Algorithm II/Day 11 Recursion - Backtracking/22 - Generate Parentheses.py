class Solution:
    def generateParenthesis(self, n: int) -> List[str]:  # 70.58% 96.49%
        def helper(part, left, right, arr=[]):
            if left:
                helper(part+'(', left-1, right)
            if right > left:
                helper(part+')', left, right-1)
            if not right:
                arr.append(part)
            return arr
        return helper('', n, n)
