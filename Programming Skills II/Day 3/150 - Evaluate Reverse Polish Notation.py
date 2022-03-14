class Solution:
    def evalRPN(self, tokens: List[str]) -> int:  # 9.10% 36.88%
        stack = []
        for token in tokens:
            if token.strip('-+').isdigit():
                stack.append(token)
            else:
                if len(stack) == 1:
                    stack.append((-1 if token == '-' else 1)*int(stack.pop()))
                    continue
                second, first = int(stack.pop()), int(stack.pop())
                if token == '+':
                    stack.append(first+second)
                elif token == '-':
                    stack.append(first-second)
                elif token == '*':
                    stack.append(first*second)
                else:
                    stack.append(first/second)
        return int(stack.pop())
