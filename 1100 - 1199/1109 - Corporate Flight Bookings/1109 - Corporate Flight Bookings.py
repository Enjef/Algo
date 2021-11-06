class Solution:
    def corpFlightBookings(
            self,
            bookings: List[List[int]],
            n: int) -> List[int]:  # 82.90% 35.10%
        out = [0]*(n+1)
        for item in bookings:
            out[item[0]-1] += item[2]
            out[item[1]] -= item[2]
        for i in range(1, n):
            out[i] += out[i-1]
        return out[:n]

    def corpFlightBookings_best_speed(
            self,
            bookings: List[List[int]],
            n: int) -> List[int]:
        array = [0]*(n+2)
        for f, l, s in bookings:
            array[f] += s
            array[l+1] -= s
        return list(accumulate(array))[1:-1]

    def corpFlightBookings_best_memory(
            self,
            bookings: List[List[int]],
            n: int) -> List[int]:
        res = [0]*n
        for f, l, s in bookings:
            res[f-1] += s
            if l < n:
                res[l] -= s
        return accumulate(res)
