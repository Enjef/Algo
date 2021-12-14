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

    def findTheWinner_best_speed(self, n: int, k: int) -> int:
        ans = 0
        for i in range(1, n+1):
            ans = (ans + k) % i
        return ans + 1

    def findTheWinner_3d_best_speed(self, n: int, k: int) -> int:
        circle, start = list(range(1,n+1)), 0
        while len(circle) > 1:
            start = (start + k - 1) % len(circle)
            circle.pop(start)
            start %= len(circle)
        return circle[0]

    def findTheWinner_best_memory(self, n: int, k: int) -> int:
        q = collections.deque()
        for i in range(n):
            q.append(i+1)
        while len(q) > 1:
            for i in range(k-1):
                q.append(q.popleft())
            q.popleft()
        return q.pop()
