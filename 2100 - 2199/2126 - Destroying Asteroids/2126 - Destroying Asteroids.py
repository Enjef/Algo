class Solution:
    def asteroidsDestroyed(
            self, mass: int, asteroids: List[int]) -> bool:  # 27.84% 69.42%
        asteroids.sort()
        for cur in asteroids:
            if mass >= cur:
                mass += cur
            else:
                return False
        return True

    def asteroidsDestroyed_best_speed(
            self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        m = asteroids[-1]
        for i in asteroids:
            if mass < i:
                return False
            if mass >= m:
                return True
            mass += i
        return True

    def asteroidsDestroyed_top_10_memory(
            self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort(reverse=True)
        while asteroids and asteroids[-1] <= mass:
            mass += asteroids.pop()
        return len(asteroids) == 0
