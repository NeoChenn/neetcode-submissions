class MyStack:

    #Queue follows first in first out.
    #Stack follows last in first out
    #So to implement a stack using queues, 

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        return self.queue1.pop()

    def top(self) -> int:
        return self.queue1[-1]

    def empty(self) -> bool:
        if len(self.queue1) == 0:
            return True
        else: 
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()