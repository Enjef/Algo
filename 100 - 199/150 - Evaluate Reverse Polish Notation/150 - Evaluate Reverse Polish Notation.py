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

    def evalRPN_best_speed(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in {"+", "-", "*", "/"}:
                stack.append(int(i))
            else:
                r, l = stack.pop(), stack.pop()
                if i == "+":
                    stack.append(l + r)
                elif i == "-":
                    stack.append(l - r)
                elif i == "*":
                    stack.append(l * r)
                else:
                    stack.append(int(l / r))
        return stack.pop()

    def evalRPN_best_memory(self, tokens: List[str]) -> int:
        def sign(a):
            if a == 0:
                return 1
            else:
                return int(a/abs(a))

        def operation(a, b, operator):
            if operator == '+':
                return a+b
            if operator == '-':
                return a-b
            if operator == '*':
                return a*b
            if operator == '/':
                return abs(a)//abs(b)*sign(a)*sign(b)

        ans = []
        operators = ['+', '-', '*', '/']
        for tok in tokens:
            if tok not in operators:
                ans.append(int(tok))
            else:
                b = ans.pop(-1)
                a = ans.pop(-1)
                ans.append(operation(a, b, tok))
        return ans[0]
