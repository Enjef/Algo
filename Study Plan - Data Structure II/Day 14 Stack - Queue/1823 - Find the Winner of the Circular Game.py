class Solution:
    def findTheWinner(self, n: int, k: int) -> int:  # 55.12% 45.84%
        circle = list(range(1, n+1))
        while len(circle) > 1:
            index = k
            if index > len(circle):
                index %= len(circle)
            if index == 0:
                circle.pop()
            else:
                circle = circle[index:] + circle[:index-1] 
        return circle[0]
