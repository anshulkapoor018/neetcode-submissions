class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])
        l = 0
        r = len(values) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2

            time, value = values[mid]

            if time <= timestamp:
                res = value
                l = mid + 1
            else: 
                r = mid - 1

        return res
        
