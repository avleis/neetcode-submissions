class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
            else:
                value_2 = stack.pop()
                value_1 = stack.pop()

                match token:
                    case '+':
                        stack.append(value_1 + value_2)
                    case '-':
                        stack.append(value_1 - value_2)
                    case '*':
                        stack.append(value_1 * value_2)
                    case '/':
                        stack.append(int(value_1 / value_2))

        return stack[-1]