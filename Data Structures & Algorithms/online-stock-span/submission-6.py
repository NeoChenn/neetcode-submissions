class StockSpanner:

    def __init__(self):
        self.monoStack = [[0, 100001]]
        self.index = 0

    def next(self, price: int) -> int:
        self.index += 1
        while self.monoStack and price >= self.monoStack[-1][1]:
            self.monoStack.pop()
        res = self.index - self.monoStack[-1][0]
        self.monoStack.append([self.index, price])
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)