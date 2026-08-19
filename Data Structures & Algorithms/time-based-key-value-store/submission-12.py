class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        values = self.timeMap[key] #it's sorted. binary search to find value
        #[1, 4, 5, 7, 9] timestamp = 6
        #if timestamp in values, return that value. Otherwise, the biggest that's smaller than timestamp
        #if no values or timestamp is smaller than the smallest value, return ""
        if len(values) == 0 or timestamp < values[0][1]:
            return ""
        
        l, r, maxIndex = 0, len(values) - 1, 0
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] > timestamp:
                r = mid - 1
            else:
                maxIndex = max(maxIndex, mid)
                l = mid + 1
        return values[maxIndex][0]

