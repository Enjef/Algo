class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                out.append("FizzBuzz")
                continue
            if i % 5 == 0:
                out.append("Buzz")
                continue
            if i % 3 == 0:
                out.append("Fizz")
                continue
            out.append(str(i))
        return out
