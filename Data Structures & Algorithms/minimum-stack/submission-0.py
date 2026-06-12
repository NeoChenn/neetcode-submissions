class MinStack:

    #[3, 5, 1, 2, 5, 7]

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)        

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        lowest = 2**31
        tempStack = self.stack.copy()
        while len(tempStack) > 0:
            lowest = min(lowest, tempStack.pop())
        return lowest