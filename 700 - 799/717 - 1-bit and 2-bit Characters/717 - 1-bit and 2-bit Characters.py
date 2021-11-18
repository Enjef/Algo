class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:  # 86.25% 44.84%
        size = len(bits)
        if size == 1:
            return True
        i = 0
        while i < size:   
            i += bits[i] + 1
            remaining_bits = size - i
            if remaining_bits == 2:
                return not bits[-2]
            if remaining_bits == 1:
                return True

    def isOneBitCharacter_best_speed(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return i <= len(bits)-1

    def isOneBitCharacter_best_memory(self, bits: List[int]) -> bool:
        if not bits:
            return False
        n = len(bits)
        i = 0
        while i < n:
            if i == n-1:
                return True
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return False     
