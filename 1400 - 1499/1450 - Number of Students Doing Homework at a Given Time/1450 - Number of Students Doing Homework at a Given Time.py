class Solution:
    def busyStudent(
            self,
            startTime:
            List[int],
            endTime: List[int],
            queryTime: int
         ) -> int:  # 77.08%  83.35% same as best
        count = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                count += 1
        return count

    def busyStudent_short(
            self,
            startTime: List[int],
            endTime: List[int],
            queryTime: int) -> int:  # 77.08% 20.95%
        return sum(
            [
                1 if startTime[i] <= queryTime <= endTime[i] else 0
                for i in range(len(startTime))
            ])
