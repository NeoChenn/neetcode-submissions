class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] #["-", "4", "*", "3", "+", "2", "1"]

        for value in tokens:
            if value == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif value == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1) - int(num2))
            elif value == '*':
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif value == '/':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(int(num1) / int(num2)))
            else:
                stack.append(value)

        return int(stack[0])