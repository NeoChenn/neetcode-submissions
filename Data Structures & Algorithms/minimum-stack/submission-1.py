class MinStack:

    #[3, 5, 1, 2, 5, 7]

    def __init__(self):
        self.stack = []
        self.lowest = 2**31

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.lowest = min(self.lowest, val)        

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:

        return min(self.stack)