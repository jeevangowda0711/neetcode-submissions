class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in ['+', '-', '*', '/']:
                stack.append(i)
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if i == '+':
                    stack.append(int(operand1) + int(operand2))
                elif i == '-':
                    stack.append(int(operand1) - int(operand2))
                elif i == '*':
                    stack.append(int(operand1) * int(operand2))
                else:
                    stack.append(int(int(operand1) / int(operand2)))
        return int(stack.pop())