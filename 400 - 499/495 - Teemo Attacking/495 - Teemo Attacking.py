class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if duration == 0:
            return 0
        out = 0
        for i in range(1, len(timeSeries)):
            diff = timeSeries[i] - timeSeries[i-1]
            if diff < duration:
                out += diff
            elif diff >= duration:
                out += duration
        return out + duration
