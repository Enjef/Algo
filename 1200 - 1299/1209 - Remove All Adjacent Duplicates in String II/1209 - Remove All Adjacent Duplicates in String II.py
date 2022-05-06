class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:  # 97.11% 17.87%
        stack = []
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
                    continue
            else:
                stack.append([char, 1])
        return ''.join([x[0]*x[1] for x in stack])

    def removeDuplicates_best_speed(self, s: str, k: int) -> str:
        if not s or k <= 1:
            return ''
        let_counter = 0
        cur_letter = None
        result = []
        for c in s:
            if not cur_letter:
                cur_letter = c
            if c == cur_letter:
                let_counter += 1
                if let_counter == k:
                    if result:
                        prev_letter_counts = result.pop()
                        cur_letter = prev_letter_counts[0]
                        let_counter = prev_letter_counts[1]
                    else:
                        cur_letter = None
                        let_counter = 0
            else:
                result.append((cur_letter, let_counter))
                cur_letter = c
                let_counter = 1
        if cur_letter and let_counter:
            result.append((cur_letter, let_counter))
        return ''.join([r[0]*r[1] for r in result])

    def removeDuplicates_best_memory(self, s: str, k: int) -> str:
        if len(s) < k:
            return s
        counts = defaultdict(int)
        left = right = 0
        while right < len(s):
            counts[s[right]] += 1
            if counts[s[right]] == k:
                s = s[:left] + s[right + 1:]
                if left > 0:
                    left = max(0, left - k - 1)
                right = left
                counts = defaultdict(int)
                continue
            if right - left + 1 == k:
                counts[s[left]] -= 1
                left += 1
            right += 1
        return s
