class Solution:
    def convertTime(self, current: str, correct: str) -> int:  # 50.00% 66.67%
        def transform(time):
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes
        
        diff = transform(correct) - transform(current)
        out = 0
        for part in [60, 15, 5, 1]:
            out += diff // part
            diff = diff % part
        return out
