class TimeMap:

    def __init__(self):
        self.myMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.myMap:
            self.myMap[key].append([value, timestamp])
        else:
            self.myMap[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.myMap:
            return ""
        values = self.myMap[key]
        l, r = 0, len(values) - 1
        val = ""

        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                l = mid + 1
                val = values[mid][0]
            elif values[mid][1] > timestamp:
                r = mid - 1
        
        return val

        #values = [["happy", 1], ["sad", 2], ["angry", 2], ["lonely", 3]]
        #       = [1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5]
        #return most recent value not exceeding given timestamp, prev_timestamp <= timestamp
        #if mid <= ts, move right
        #elif mid > ts, move left
