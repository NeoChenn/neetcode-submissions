class StockSpanner:

    def __init__(self):
        self.spans = [(0, 0)]
        self.index = 1

    def next(self, price: int) -> int:
        #monotonic decreasing stack
        while len(self.spans) > 1 and price >= self.spans[-1][0]:
            self.spans.pop()

        res = self.index - self.spans[-1][1]
        self.spans.append((price, self.index))
        self.index += 1
        return res

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)