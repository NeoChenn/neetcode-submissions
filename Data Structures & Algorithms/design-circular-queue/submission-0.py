class MyCircularQueue:

    def __init__(self, k: int):
        self.head, self.tail = 0, 0 
        self.queue = [-1] * k
        #array with modulo operator to "wrap around"
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.tail % len(self.queue)] = value
        self.tail += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.head % len(self.queue)] = -1
        self.head += 1
        return True

    def Front(self) -> int:
        return self.queue[self.head % len(self.queue)]

    def Rear(self) -> int:
        return self.queue[(self.tail - 1) % len(self.queue)]

    def isEmpty(self) -> bool:
        return self.queue[self.head % len(self.queue)] == -1

    def isFull(self) -> bool:
        return self.queue[self.tail % len(self.queue)] != -1


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()