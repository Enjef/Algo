class Solution:
    # 59.12% 32.99% (69.56% 32.99%)
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        n = len(energy)
        res = 0
        for i in range(n):
            x = 0
            if initialEnergy <= energy[i]:
                res += energy[i] - initialEnergy + 1
            if initialExperience <= experience[i]:
                x = experience[i] - initialExperience + 1
                res += x
            initialEnergy = max(initialEnergy - energy[i], 1)
            initialExperience += experience[i] + x
        return res


class Solution_best_speed:
    def minNumberOfHours_1st(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        curr_eng, curr_exp, ans = initialEnergy, initialExperience, 0
        for x, y in zip(energy, experience):
            if curr_eng <= x:
                ans += x + 1 - curr_eng
                curr_eng = x + 1
            if curr_exp <= y:
                ans += y + 1 - curr_exp
                curr_exp = y + 1
            curr_eng -= x
            curr_exp += y
        return ans


class Solution_best_memory:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        time = 0
        for i in range(len(energy)):
            if energy[i] >= initialEnergy:
                time += energy[i]-initialEnergy+1
                initialEnergy += energy[i]-initialEnergy+1
            initialEnergy -= energy[i]
            if experience[i] >= initialExperience:
                time += experience[i]-initialExperience+1
                initialExperience += experience[i]-initialExperience+1
            initialExperience += experience[i]
        return time
