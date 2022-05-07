class Solution:
    def shiftingLetters(
            self, s: str, shifts: List[int]) -> str:  # 30.54% 89.08%
        n = len(s)
        alp = 'abcdefghijklmnopqrstuvwxyz'
        alp_len = len(alp)
        for i in range(n-2, -1, -1):
            shifts[i] += shifts[i+1]
        out = []
        for i, char in enumerate(s):
            idx = (alp.index(char)+shifts[i]) % alp_len
            out.append(alp[idx])
        return ''.join(out)

    def shiftingLetters_2nd_best_speed(self, s: str, shifts: List[int]) -> str:
        alpha = list(string.ascii_lowercase)
        length = len(alpha)
        answer = list(s)
        move_sum = 0
        for i in range(len(shifts)-1, -1, -1):
            move_sum += shifts[i]
            answer[i] = alpha[(ord(answer[i]) - ord('a') + move_sum) % length]
        return ''.join(answer)

    def shiftingLetters_3d_best_speed(self, s: str, shifts: List[int]) -> str:
        c = sum(shifts)
        ans = ''
        for i, e in enumerate(s):
            ans += chr((ord(e) - 97 + c) % 26 + 97)
            c -= shifts[i]
        return ans

    def shiftingLetters_best_memory(self, s: str, shifts: List[int]) -> str:
        for i in range(len(shifts)-2, -1, -1):
            shifts[i] = (shifts[i] + shifts[i+1]) % 26
        ans = [chr(((ord(c)-ord('a') + shifts[i])%26)+ord('a')) for i, c in enumerate(s)]
        return ''.join(ans)


OFFSET = ord('a')
ALPHABET = [chr(OFFSET + i) for i in range(26)]

def get_postfix_sum(nums):
    prev = 0
    for i in range(len(nums)-1, -1, -1):
        nums[i] += prev
        prev = nums[i]
    return nums


class Solution_best_speed:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shifts = get_postfix_sum(shifts)
        return "".join(
            ALPHABET[(ord(c) - OFFSET + shift) % 26]
            for c, shift in zip(s, shifts)
        )
