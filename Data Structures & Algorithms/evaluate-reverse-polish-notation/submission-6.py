class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in ['+', '-', '*', '/']:
                stack.append(int(i))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if i == '+':
                    stack.append(operand1 + operand2)
                elif i == '-':
                    stack.append(operand1 - operand2)
                elif i == '*':
                    stack.append(operand1 * operand2)
                else:
                    stack.append(int(operand1 / operand2))
        return stack.pop()