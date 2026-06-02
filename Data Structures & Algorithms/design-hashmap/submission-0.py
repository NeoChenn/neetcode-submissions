class MyHashMap:

    def __init__(self):
        self.keyArr = []
        self.valueArr = []

    def put(self, key: int, value: int) -> None:
        if key in self.keyArr:
            self.valueArr[self.keyArr.index(key)] = value
            return
        self.keyArr.append(key)
        self.valueArr.append(value)

    def get(self, key: int) -> int:
        if key not in self.keyArr:
            return -1
        return self.valueArr[self.keyArr.index(key)]

    def remove(self, key: int) -> None:
        if key in self.keyArr:
            self.valueArr.remove(self.valueArr[self.keyArr.index(key)])
            self.keyArr.remove(key)
            


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)