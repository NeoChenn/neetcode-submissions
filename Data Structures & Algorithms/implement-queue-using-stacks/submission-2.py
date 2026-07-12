class MyQueue:

    def __init__(self):
        self.stack1 = []     #[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]
        self.stack2 = []

    def push(self, x: int) -> None:
        #push to stack1
        self.stack1.append(x)

    def pop(self) -> int:
        #if stack2 empty, push all of stack1 to stack2
        #pop from stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        #stack2[-1]
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        #both stack1 and stack2 are empty
        return not self.stack1 and not self.stack2

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()