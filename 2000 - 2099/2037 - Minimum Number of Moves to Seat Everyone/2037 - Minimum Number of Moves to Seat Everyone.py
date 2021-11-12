class Solution:
    def minMovesToSeat(
            self,
            seats: List[int],
            students: List[int]) -> int:  # 96.59% 61.57%
        seats.sort()
        students.sort()
        return sum([abs(x-y) for x, y in zip(seats, students)])

    def minMovesToSeat_best_speed(
            self,
            seats: List[int],
            students: List[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)
        return sum(abs(seats[i] - students[i]) for i in range(len(seats)))

    def minMovesToSeat_best_memory(
            self,
            seats: List[int],
            students: List[int]) -> int:
        seats.sort()
        students.sort()
        result = 0
        for i in range(len(students)):
            result = result + abs(seats[i]-students[i])
        return result
