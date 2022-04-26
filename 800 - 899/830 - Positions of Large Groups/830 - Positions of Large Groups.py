class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:  # 96.11% 74.49%
        result = []
        cur = ''
        start = 0
        for i, char in enumerate(s):
            if char == cur:
                continue
            else:
                if i - start > 2:
                    result.append([start, i-1])
                start = i
                cur = char
        else:
            if i - start > 1:
                result.append([start, i])
        return result

    def largeGroupPositions_v2(self, s):  # 95.18% 74.49%
        result = []
        cur = ''
        start = 0
        for i, char in enumerate(s):
            if char == cur:
                continue
            else:
                if i - start > 2:
                    result.append([start, i-1])
                start = i
                cur = char
        if i - start > 1:
            result.append([start, i])
        return result

    def largeGroupPositions_best_speed(self, s: str) -> List[List[int]]:
        if not s:
            return None
        ans = []
        current_char = s[0]
        current_start = 0
        current_length = 1
        for i in range(1, len(s)):
            c = s[i]
            if c == current_char:
                current_length += 1
            else:
                if current_length >= 3:
                    ans.append([current_start, i - 1])
                current_start = i
                current_char = c
                current_length = 1
        if current_length >= 3:
            ans.append([current_start, len(s)-1])
        return ans

    def largeGroupPositions_best_memory(self, s: str) -> List[List[int]]:
        repeat_count = 1
        repeat_intervals = []
        s += ' '
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                if repeat_count >= 3:
                    repeat_intervals.append([i-repeat_count, i-1])
                repeat_count = 0
            repeat_count += 1
        return repeat_intervals
