class Solution:
    def reverseString(self, s):  # 94.52%  57.50%
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s

    def reverseString_study_plan_day_4(
            self,
            s: List[str]) -> None:  # 20.05% 99.90%
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[-1-i] = s[-1-i], s[i]
        return
