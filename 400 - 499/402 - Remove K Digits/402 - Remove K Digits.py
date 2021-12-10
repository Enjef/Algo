class Solution:
    def removeKdigits(self, num: str, k: int) -> str:  # 85.95% 33.59%
        stack = []
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        while k > 0:
            stack.pop()
            k -= 1
        i = 0
        while i < len(stack) and stack[i] == '0':
            i += 1
        return ''.join(stack[i:]) if stack[i:] else '0'

    def removeKdigits_best_speed(self, num: str, k: int) -> str:
        numStack = []
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1
            numStack.append(digit)
        finalStack = numStack[:-k] if k else numStack
        return ''.join(finalStack).lstrip('0') or '0'

    def removeKdigits_best_memory(self, num: str, k: int) -> str:
        index = 0
        num_len = len(num)
        if k == num_len:
            return '0'
        result = ''
        while index + k < num_len:
            i = 1
            offset = 0
            while i <= k:
                if num[index+offset] > num[index+i]:
                    offset = i
                i += 1
            result += num[index+offset]
            k -= offset
            index += offset + 1
        return str(int(result))
