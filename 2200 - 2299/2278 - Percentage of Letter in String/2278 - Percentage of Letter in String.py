class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:  # 70.81% 59.33%
        return int(s.count(letter) / len(s) * 100)

    def percentageLetter_best_speed(self, s: str, letter: str) -> int:
        c = s.count(letter)
        if c == 0:
            return 0
        else:
            return int((c/len(s))*100)

    def percentageLetter_best_memory(self, s: str, letter: str) -> int:
        x = s.count(letter)
        return (100*x)//len(s)
