class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in '+-*/':
                last_number = stack.pop()
                perlast_number = stack.pop()

                match token:
                    case '+':
                        perlast_number += last_number
                    case '-':
                        perlast_number -= last_number
                    case '*':
                        perlast_number *= last_number
                    case '/':
                        perlast_number = int(perlast_number / last_number)
                
                stack.append(perlast_number)
            else:
                stack.append(int(token))

        return stack[0]