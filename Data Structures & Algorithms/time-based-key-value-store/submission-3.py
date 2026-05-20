class TimeMap:

    def __init__(self):

        # Store:
        # key -> list of [value, timestamp]
        self.store = {}


    def set(self, key: str, value: str, timestamp: int) -> None:

        # Create list for key if it doesn't exist
        if key not in self.store:
            self.store[key] = []

        # Append value with timestamp
        # Timestamps are inserted in increasing order
        self.store[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:

        # Get all values for this key
        values = self.store.get(key, [])

        left = 0
        right = len(values) - 1

        result = ""

        # Binary search for closest timestamp <= target timestamp
        while left <= right:

            mid = (left + right) // 2

            value, time = values[mid]

            # Valid timestamp
            if time <= timestamp:

                # Store current best answer
                result = value

                # Try finding a later valid timestamp
                left = mid + 1

            else:
                # Timestamp too large
                right = mid - 1

        return result