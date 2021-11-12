class Solution:
    def minMovesToSeat(
            self,
            seats: List[int],
            students: List[int]) -> int:  # 96.59% 61.57%
        seats.sort()
        students.sort()
        return sum([abs(x-y) for x, y in zip(seats, students)])
