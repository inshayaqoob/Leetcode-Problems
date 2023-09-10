class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.data:
            values = self.data[key]
            left, right = 0, len(values) - 1

            while left <= right:
                mid = left + (right - left) // 2
                ts, val = values[mid]

                if ts <= timestamp:
                    left = mid + 1
                else:
                    right = mid - 1

            if right >= 0:
                return values[right][1]

        return ""
