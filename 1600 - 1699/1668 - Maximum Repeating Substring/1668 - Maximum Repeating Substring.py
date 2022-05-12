class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:  # 49.02% 62.70%
        m, n = len(sequence), len(word)
        index_list = []
        for i in range(m):
            if sequence[i:i+n] == word:
                index_list.append(i)
        max_len = 0
        for idx in index_list:
            cur_len = 0
            cur = idx
            while cur in index_list:
                cur += n
                cur_len += 1
            max_len = max(max_len, cur_len)
        return max_len

    def maxRepeating_best_speed(self, sequence: str, word: str) -> int:
        i = 0
        bestK = k = 0
        for i in range(len(word)):
            j = i
            k = 0
            bestKStartHere = 0
            while j < len(sequence):
                if sequence[j:].startswith(word):
                    k += 1
                    bestKStartHere = max(bestKStartHere, k)
                else:
                    k = 0
                j += len(word)
            bestK = max(bestK, bestKStartHere)
        return bestK

    def maxRepeating_2nd_best_speed(self, sequence: str, word: str) -> int:
        if len(sequence) < len(word):
            return 0
        k = 1
        while word * k in sequence:
            k += 1
        return k - 1

    def maxRepeating_3d_best_speed(self, sequence: str, word: str) -> int:
        s = word
        count = 0
        while s in sequence:
            s += word
            count += 1
        return count

    def maxRepeating_best_memory(self, seq: str, word: str) -> int:
        max_count = 0
        string = word
        while True:
            if string in seq:
                max_count += 1
                string += word
            else:
                break
        return max_count
