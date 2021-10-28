class Solution:
    def distanceBetweenBusStops(
            self,
            distance: List[int],
            start: int,
            destination: int) -> int:  # 85.49% 37.73%
        if start > destination:
            start, destination = destination, start
        return min(
            sum(distance[start:destination]),
            sum(distance[:start])+sum(distance[destination:])
        )

    def distanceBetweenBusStops_best_speed(
            self,
            distance: List[int],
            start: int,
            destination: int) -> int:
        total = sum(distance)
        s = min(start, destination)
        e = max(start, destination)
        d1 = sum(distance[s:e])
        return min(d1, total-d1)
