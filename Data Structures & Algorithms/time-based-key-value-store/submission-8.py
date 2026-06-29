class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        values = self.timemap[key] #[1, 1, 2, 2, 2, 3, 3, 3, 4, 5]
        idx = None
        i, j = 0, len(values) - 1
        while i <= j:
            mid = (i + j) // 2
            if values[mid][1] <= timestamp:
                idx = mid
                i = mid + 1
            else:
                j = mid - 1
        if idx is None:
            return ""
        return values[idx][0]
