class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                post = int(stack.pop())
                pre = int(stack.pop())
                stack.append(str(pre + post))

            elif c == "*":
                post = int(stack.pop())
                pre = int(stack.pop())
                stack.append(str(pre * post))

            elif c == "-":
                post = int(stack.pop())
                pre = int(stack.pop())
                stack.append(str(pre - post))

            elif c == "/":
                post = int(stack.pop())
                pre = int(stack.pop())
                if pre / post < 0:
                    stack.append(str(math.ceil(pre / post)))
                else:
                    stack.append(str(pre // post))
            else:
                stack.append(c)
        return int(stack.pop())