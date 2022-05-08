class Solution:
    def makeFancyString(self, s: str) -> str:  # 73.33% 18.02%
        stack = []
        for char in s:
            if len(stack) > 1 and char == stack[-1] and char == stack[-2]:
                continue
            stack.append(char)
        return ''.join(stack)

    def makeFancyString_best_speed(self, s: str) -> str:
        output = ''
        prev_c = ''
        prev_o = 1
        for i in s:
            if i == prev_c:
                if prev_o < 2:
                    prev_o += 1
                    output += prev_c
            else:
                prev_c = i
                prev_o = 1
                output += prev_c
        return output

    def makeFancyString_4th_best_speed(self, s):
        x = ''
        a, b = '*', '*'
        for c in s:
            if not a == b == c:
                x += c
            a, b = b, c
        return x

    def makeFancyString_best_memory(self, s: str) -> str:
        for i in set(s):
            if s.count(i) > 2:
                while i*3 in s:
                    s = s.replace(i*3, i*2)
        return s
